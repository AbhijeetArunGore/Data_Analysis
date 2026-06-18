import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import RobustScaler
from statsmodels.tsa.stattools import adfuller
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Constants
INPUT_FILE = r'C:\Users\abhis\Desktop\DA\btc_data_3650d_5m.csv'
OUTPUT_FILE = r'C:\Users\abhis\Desktop\DA\processed_data\btc_processed_final.parquet'

def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_atr(df, period=14):
    high_low = df['High'] - df['Low']
    high_close = np.abs(df['High'] - df['Close'].shift())
    low_close = np.abs(df['Low'] - df['Close'].shift())
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return tr.rolling(window=period).mean()

def calculate_adx(df, period=14):
    df = df.copy()
    df['up_move'] = df['High'].diff()
    df['down_move'] = df['Low'].diff().apply(lambda x: -x)
    
    df['+DM'] = np.where((df['up_move'] > df['down_move']) & (df['up_move'] > 0), df['up_move'], 0)
    df['-DM'] = np.where((df['down_move'] > df['up_move']) & (df['down_move'] > 0), df['down_move'], 0)
    
    tr = calculate_atr(df, 1) # True Range
    df['TR_smooth'] = tr.rolling(window=period).sum()
    df['+DM_smooth'] = df['+DM'].rolling(window=period).sum()
    df['-DM_smooth'] = df['-DM'].rolling(window=period).sum()
    
    df['+DI'] = 100 * (df['+DM_smooth'] / df['TR_smooth'])
    df['-DI'] = 100 * (df['-DM_smooth'] / df['TR_smooth'])
    df['DX'] = 100 * (np.abs(df['+DI'] - df['-DI']) / (df['+DI'] + df['-DI']))
    return df['DX'].rolling(window=period).mean()

def preprocess_data():
    print("Loading raw data...")
    # Load raw data
    df = pd.read_csv(INPUT_FILE)
    
    # 1. Data Cleaning
    print("Cleaning data...")
    df['Date'] = pd.to_datetime(df['Date'], utc=True)
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    
    # Identify gaps and ffill
    full_range = pd.date_range(start=df.index.min(), end=df.index.max(), freq='5min')
    df = df.reindex(full_range)
    df[['Open', 'High', 'Low', 'Close']] = df[['Open', 'High', 'Low', 'Close']].ffill(limit=2)
    df['Volume'] = df['Volume'].fillna(0)
    df.dropna(inplace=True)
    
    # Outlier removal (3 standard deviation rolling Z-score)
    print("Removing outliers...")
    rolling_mean = df['Close'].rolling(window=20).mean()
    rolling_std = df['Close'].rolling(window=20).std()
    z_score = (df['Close'] - rolling_mean) / rolling_std
    df = df[np.abs(z_score) < 3]
    
    # 2. Feature Engineering
    print("Engineering features...")
    # EMA Trend
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['EMA_50'] = df['Close'].ewm(span=50, adjust=False).mean()
    df['EMA_200'] = df['Close'].ewm(span=200, adjust=False).mean()
    df['Price_EMA_Ratio'] = df['Close'] / df['EMA_200']
    
    # Momentum
    df['RSI_14'] = calculate_rsi(df['Close'], period=14)
    df['ROC_12'] = df['Close'].pct_change(periods=12) * 100
    
    # Volatility
    df['ATR_14'] = calculate_atr(df, period=14)
    df['ADX_14'] = calculate_adx(df, period=14)
    
    # Liquidity & Flow
    df['ADT_24h'] = (df['Close'] * df['Volume']).rolling(window=288).mean() # 288 periods = 24h
    df['VWAP'] = (df['Close'] * df['Volume']).cumsum() / df['Volume'].cumsum()
    
    # On-Balance Volume (OBV)
    df['OBV'] = (np.sign(df['Close'].diff()) * df['Volume']).fillna(0).cumsum()
    
    # 3. Stationarity Transformation
    print("Converting to Log Returns...")
    df['Log_Returns'] = np.log(df['Close'] / df['Close'].shift(1))
    
    # Drop intermediate NaNs created by rolling indicators
    df.dropna(inplace=True)
    
    # 4. Scaling
    print("Applying Robust Scaling...")
    features_to_scale = ['RSI_14', 'ROC_12', 'ATR_14', 'ADX_14', 'Price_EMA_Ratio', 'ADT_24h', 'OBV', 'VWAP']
    scaler = RobustScaler()
    df[features_to_scale] = scaler.fit_transform(df[features_to_scale])
    
    # 5. ADF Test for Stationarity
    print("\nADF Test for Stationarity (p < 0.05 is stationary):")
    for feat in ['Log_Returns', 'RSI_14', 'ADX_14']:
        result = adfuller(df[feat].dropna().iloc[:10000]) # Use subset for speed
        print(f" - {feat}: p-value = {result[1]:.4f}")
    
    # 6. Save as Parquet
    print(f"\nSaving processed data to {OUTPUT_FILE}...")
    df.to_parquet(OUTPUT_FILE)
    print("Process complete!")

if __name__ == "__main__":
    if os.path.exists(INPUT_FILE):
        preprocess_data()
    else:
        print(f"Error: Could not find {INPUT_FILE}")

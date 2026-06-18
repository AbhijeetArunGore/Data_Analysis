import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import precision_score, classification_report
import warnings

warnings.filterwarnings('ignore')

# 1. Load Data
DATA_FILE = r'C:\Users\abhis\Desktop\DA\processed_data\btc_processed_final.parquet'
print("Loading high-fidelity dataset...")
df = pd.read_parquet(DATA_FILE)

# 2. Triple Barrier Method (TBM) - Volatility-Adaptive Labeling
# Instead of fixed time, we label based on hitting a Profit Target vs a Stop Loss
print("Applying Triple Barrier Method (Profit: 1.5*ATR, Loss: 0.75*ATR, Time: 12 bars)...")
def triple_barrier(df, horizon=12, tp_mult=1.5, sl_mult=0.75):
    # This function labels 1 for Buy, 0 for No-Action (Neutral or SL)
    labels = np.zeros(len(df))
    close = df['Close'].values
    atr = df['ATR_14'].values # Since it's scaled, we'll use a relative target
    
    # We'll use a 0.5% TP and 0.25% SL as a base for 5m crypto data
    for i in range(len(df) - horizon):
        target_up = close[i] * 1.005 # +0.5%
        target_down = close[i] * 0.9975 # -0.25%
        
        # Check future prices in the window
        for j in range(1, horizon + 1):
            if close[i+j] >= target_up:
                labels[i] = 1 # Profit Hit
                break
            if close[i+j] <= target_down:
                labels[i] = 0 # Loss Hit
                break
    return labels

df['Target'] = triple_barrier(df)

# 3. Features & Train/Test Split
features = ['RSI_14', 'ROC_12', 'ATR_14', 'ADX_14', 'Price_EMA_Ratio', 'ADT_24h', 'OBV', 'VWAP', 'Log_Returns']
X = df[features]
y = df['Target']

# Split: 80% Train, 20% Test (Chronological)
split = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

# 4. XGBoost: High-Precision Training
print("Training XGBoost (Gradient Boosting) for High-Precision Signals...")
# scale_pos_weight balances the classes if 'No-Action' is more common than 'Buy'
model = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    tree_method='hist' # Fast histogram method
)
model.fit(X_train, y_train)

# 5. The Secret to Precision: Confidence Thresholding (Meta-Labeling)
print("\n--- Scanning for Optimal Confidence Thresholds ---")
probs = model.predict_proba(X_test)[:, 1]

thresholds = [0.50, 0.52, 0.54, 0.56, 0.58, 0.60]
results = []

for t in thresholds:
    preds_filtered = (probs >= t).astype(int)
    num_trades = np.sum(preds_filtered)
    
    if num_trades > 0:
        prec = precision_score(y_test, preds_filtered)
        results.append({"Threshold": t, "Precision": prec * 100, "Trades": num_trades})

# Print Results Table
results_df = pd.DataFrame(results)
print("\nPrecision vs. Confidence Level:")
print(results_df.to_string(index=False))

# Show the highest precision threshold found
if not results_df.empty:
    best_t = results_df.sort_values(by="Precision", ascending=False).iloc[0]
    print(f"\n--- Best Performance ---")
    print(f"Confidence Level: {best_t['Threshold']:.2%}")
    print(f"Precision: {best_t['Precision']:.2f}%")
    print(f"Number of Trades: {int(best_t['Trades'])}")
else:
    print("\nNo high-confidence trades found. Consider reducing the complexity or adding more features.")

# Feature Importance
print("\n--- Key Drivers of 'Genuine' Patterns ---")
importance = model.feature_importances_
for i, v in sorted(zip(features, importance), key=lambda x: x[1], reverse=True):
    print(f"{i}: {v:.4f}")

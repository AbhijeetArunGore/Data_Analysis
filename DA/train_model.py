import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, precision_score
import warnings

warnings.filterwarnings('ignore')

# 1. Load Data
DATA_FILE = r'C:\Users\abhis\Desktop\DA\processed_data\btc_processed_final.parquet'
print("Loading processed dataset...")
df = pd.read_parquet(DATA_FILE)

# 2. Define the Target (Labeling)
# Let's predict if the price will be higher 6 periods (30 minutes) from now
print("Generating Target labels (Predicting 30m ahead)...")
df['Future_Close'] = df['Close'].shift(-6)
df['Target'] = np.where(df['Future_Close'] > df['Close'], 1, 0)

# Drop rows where we don't have a future close
df.dropna(subset=['Future_Close'], inplace=True)

# 3. Select Features
features = [
    'RSI_14', 'ROC_12', 'ATR_14', 'ADX_14', 
    'Price_EMA_Ratio', 'ADT_24h', 'OBV', 'VWAP', 'Log_Returns'
]

X = df[features]
y = df['Target']

# 4. Strict Chronological Train/Test Split (No Data Leakage)
# Train on the first 80% of time, Test on the last 20%
print("Splitting data chronologically (80% Train, 20% Test)...")
split_idx = int(len(df) * 0.8)

X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# 5. Train the Model
# We limit max_depth to 5 to prevent overfitting to market noise
print("\nTraining Random Forest Classifier...")
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# 6. Evaluate Results
print("\nEvaluating Model on Test Data...")
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)

print(f"\n--- Model Results ---")
print(f"Accuracy:  {accuracy * 100:.2f}% (Overall Correctness)")
print(f"Precision: {precision * 100:.2f}% (When model says 'Buy', how often is it right?)")

print("\n--- Detailed Classification Report ---")
print(classification_report(y_test, predictions))

# 7. Feature Importance
print("--- Feature Importance ---")
importances = pd.DataFrame({
    'Feature': features,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)
print(importances.to_string(index=False))

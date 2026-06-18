# Simple price predictor based on area
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    'Area': [750, 800, 1200, 1500, 1800, 2000, 2500],
    'Price': [150000, 160000, 200000, 240000, 300000, 320000, 400000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Area']]
y = df['Price']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Take user input
area = float(input("Enter area in sqft: "))

# Predict price
predicted_price = model.predict([[area]])
print(f"Predicted Price: ${predicted_price[0]:.2f}")

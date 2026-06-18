import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'Area':[750,800,1200,1500,1800,2000,2500],
        'Price':[150000,160000,200000,240000,300000,320000,400000]}
df = pd.DataFrame(data)

X = df[['Area']]
y = df['Price']

model = LinearRegression()
model.fit(X, y)

# Accuracy on entire dataset (since it's tiny)
print("Model Accuracy (R²):", model.score(X, y))

area = float(input("Enter area in sqft: "))
pred = model.predict(pd.DataFrame([[area]], columns=['Area']))
print(f"Predicted Price: ${pred[0]:.2f}")
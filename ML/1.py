import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
# Step 3: Select Important Features
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']]
# Step 4: Handle Missing Values
df.dropna(inplace=True)
# Step 5: Convert Categorical Column 'Sex' to Numeric
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
# Step 6: Split Data into Features and Labels
X = df[['Pclass', 'Sex', 'Age', 'Fare']]
y = df['Survived']
# Step 7: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Step 8: Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)
# Step 9: Make Predictions
y_pred = model.predict(X_test)
# Step 10: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print("🎯 Model Accuracy:", accuracy)
print("\n📊 Confusion Matrix:\n", conf_matrix)
print("\n📋 Classification Report:\n", report)

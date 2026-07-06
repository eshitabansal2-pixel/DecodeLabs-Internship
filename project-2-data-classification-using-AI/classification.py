import pandas as pd 
import numpy as np 
import joblib

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

iris = load_iris()
x = iris.data
y = iris.target

print(x[:5])
print(y[:5])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("Training data:", len(x_train))
print("Testing data:", len(x_test))

model = DecisionTreeClassifier()
model.fit(x_train, y_train)
print("Model trained successfully")

y_pred = model.predict(x_test)
print("Predicted values:")
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
# New Flower data
new_flower = [[6.1, 2.5, 2.4, 1.2]]
# Predict the class
prediction = model.predict(new_flower)
# Display the result
print("Predicted Class:", prediction[0])
print("Predicted Flower:", iris.target_names[prediction[0]])
# Save the trained model
joblib.dump(model, "iris_model.pkl")
print("Model saved successfully as iris_model.pkl")
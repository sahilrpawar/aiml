# -*- coding: utf-8 -*-
"""AIHC  EXPT6 diabetes_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tmGhcAGyMP90Hb7SKIdjkBEY1swoil-x

Experiment No. 6: Predict disease risk from patient data

Name: Dhanashree Raut

Department: Comps
"""

# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load your dataset (you need to have a dataset with relevant features)
# For this example, let's assume you have a CSV file named "diabetes_dataset.csv"
# Replace 'your_data.csv' with your dataset file path.
data = pd.read_csv('diabetes.csv')

data.head()

# Split the data into features (X) and target (y)
X = data.drop('Outcome', axis=1)  # Replace 'Diabetes' with your target column name
y = data['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a random forest classifier (you can choose a different classifier as needed)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Print the results
print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{classification_rep}')
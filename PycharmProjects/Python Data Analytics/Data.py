import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import pickle


# Load Iris dataset from scikit-learn
iris = datasets.load_iris()

# Create a DataFrame
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='species')

# Combine features and target into one DataFrame
data = pd.concat([X, y], axis=1)

#print(data.head())
#print(data.info())
#print(data.describe(include='all'))

#print(data.isnull().sum())

#sns.pairplot(data, hue='species')
X = data.drop('species', axis=1)
y = data['species']

#plt.figure(figsize=(10, 8))
#sns.heatmap(data.corr(), annot=True)
#plt.show()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f'Accuracy: {acc}')

print('Classification Report:')
print(classification_report(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))


with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
    
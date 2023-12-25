import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_excel('machineLearningData5.xlsx')
labels = np.array(data.pop('successes'))

# Data not being used for ML model
data.pop("ids")
data.pop("urls")
titles = data.pop("titles")
blurbs = data.pop("blurbs")

data = np.array(data)
numRows, numCols = data.shape
training_size = int(numRows * 0.8)

training_data = data[:training_size]
training_labels = labels[:training_size]
testing_data = data[training_size:]
testing_labels = labels[training_size:]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(training_data, training_labels)

predictions = model.predict(testing_data)
accuracy = accuracy_score(testing_labels, predictions)
print("Accuracy:", accuracy)

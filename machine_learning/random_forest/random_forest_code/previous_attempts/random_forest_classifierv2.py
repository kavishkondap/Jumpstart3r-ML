# uses bagging
import pandas as pd
import numpy as np
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_excel('machineLearningData17.xlsx')
labels = np.array(data.pop('successes'))

# Data not being used for ML model
data.pop("ids")
data.pop("urls")
data.pop ('locations')
# data.pop ('titles_length')
# data.pop ('blurbs_length')
# data.pop ('titles_num_cap')
# data.pop ('blurbs_num_cap')
# data.pop ('titles_num_num')
# data.pop ('blurbs_num_num')
# data.pop ('titles_num_exc')
# data.pop ('blurbs_num_exc')
titles = data.pop("titles")
blurbs = data.pop("blurbs")

data = np.array(data)
numRows, numCols = data.shape
training_size = int(numRows * 0.8)

training_data = data[:training_size]
training_labels = labels[:training_size]
testing_data = data[training_size:]
testing_labels = labels[training_size:]

base_classifier = DecisionTreeClassifier()

model = BaggingClassifier(estimator=base_classifier, n_estimators=100, random_state=42)
model.fit(training_data, training_labels)

predictions = model.predict(testing_data)
accuracy = accuracy_score(testing_labels, predictions)
print("Accuracy:", accuracy)

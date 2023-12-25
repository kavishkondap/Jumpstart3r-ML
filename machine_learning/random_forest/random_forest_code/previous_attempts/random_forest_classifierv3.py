# additional methods of increasing accuracy

import pandas as pd
import numpy as np
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
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

# Adjust base classifier parameters
base_classifier = DecisionTreeClassifier(max_depth=5, min_samples_split=5)

# Increase number of estimators
model = BaggingClassifier(estimator=base_classifier, n_estimators=200, random_state=42)

# Feature Engineering (if applicable)
# Apply feature transformations or create new features

# Ensemble Techniques (optional)
# base_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
# model = BaggingClassifier(base_estimator=base_classifier, n_estimators=100, random_state=42)

# Cross-Validation and Parameter Tuning
# param_grid = {
#     'base_estimator__max_depth': [3, 5, 7],
#     'base_estimator__min_samples_split': [2, 5, 10],
#     'n_estimators': [100, 200, 300]
# }
# grid_search = GridSearchCV(model, param_grid, cv=5)
# grid_search.fit(training_data, training_labels)
# model = grid_search.best_estimator_

model.fit(training_data, training_labels)

predictions = model.predict(testing_data)
accuracy = accuracy_score(testing_labels, predictions)
print("Accuracy:", accuracy)

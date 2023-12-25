import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt

from sklearn import metrics

data = pd.read_excel('machineLearningData14.xlsx')
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

training_data, testing_data, training_labels, testing_labels = train_test_split (data, labels, test_size=0.2, random_state=42)
# training_data, val_data, training_labels, val_labels = train_test_split (training_data, training_labels, test_size=0.2, random_state=42)

print (training_data.shape, training_labels.shape)
# print (val_data.shape, val_labels.shape)
print (testing_data.shape, testing_labels.shape)

num_trees = 150
model_rf = RandomForestClassifier (n_estimators=num_trees, max_depth=4, class_weight='balanced')
model_rf.fit (training_data, training_labels)

training_predict = model_rf.predict (training_data)
val_predict = model_rf.predict (testing_data)

print('AUC Train: {:.4f}\nAUC Valid = {:.4f}'.format(metrics.roc_auc_score(training_labels, training_predict),
                                                     metrics.roc_auc_score(testing_labels, val_predict)))

val_labels_prob = model_rf.predict_proba (testing_data)
print (val_labels_prob)
print ('Probabilities', '\n', val_labels_prob[:10], '\n\nPredictions\n', np.array (val_predict[:10]))

print (model_rf.classes_)


# --------------------------------------------

# # Repeating same code
# y_train_prob_tree = np.stack([m.predict_proba(training_data)[:,1] for m in model_rf.estimators_])
# y_valid_prob_tree = np.stack([m.predict_proba(testing_data)[:,1] for m in model_rf.estimators_])

# # Find AUC for different levels of Trees
# train_auc_trees = [metrics.roc_auc_score(training_labels, (y_train_prob_tree[:i+1].mean(0) > 0.5).astype(int)) for i in range(num_trees)]
# valid_auc_trees = [metrics.roc_auc_score(testing_labels, (y_valid_prob_tree[:i+1].mean(0) > 0.5).astype(int)) for i in range(num_trees)]

# len(train_auc_trees), len(valid_auc_trees)

# plt.figure(figsize=(10,5))

# plt.plot(train_auc_trees, label='Train AUC')
# plt.plot(valid_auc_trees, label='Validation AUC')

# plt.ylabel('Area under Curve (AUC)')
# plt.xlabel('Number of Trees')

# plt.legend()
# plt.show()
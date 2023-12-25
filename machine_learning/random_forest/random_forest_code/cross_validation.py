import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics
import joblib
# k folds cross validation

data = pd.read_excel('machineLearningData14.xlsx')
labels = np.array(data.pop('successes'))

# Data not being used for ML model
data.pop("ids")
data.pop("urls")
data.pop ('locations')
titles = data.pop("titles")
blurbs = data.pop("blurbs")
x_train, x_val, y, y_val = train_test_split (data, labels, test_size=0.2)


n_estimators_list = list(range(10,220,50))
criterion_list = ['gini', 'entropy']
max_depth_list = list(range(5,41,10))
max_depth_list.append(None)
min_samples_split_list = [x/1000 for x in list(range(5, 41, 10))]
min_samples_leaf_list = [x/1000 for x in list(range(5, 41, 10))]
max_features_list = ['sqrt', 'log2']

params_grid = {
    'n_estimators': n_estimators_list,
    'criterion': criterion_list,
    'max_depth': max_depth_list,
    'min_samples_split': min_samples_split_list,
    'min_samples_leaf': min_samples_leaf_list,
    'max_features': max_features_list
}


num_combinations = 1
for k in params_grid.keys(): num_combinations *= len(params_grid[k])

print('Number of combinations = ', num_combinations)

def my_roc_auc_score(model, X, y): return metrics.roc_auc_score(y, model.predict(X))

model_rf = RandomizedSearchCV(estimator=RandomForestClassifier(class_weight='balanced'),
                              param_distributions=params_grid,
                              n_iter=50,
                              cv=3,
                              scoring='accuracy',
                              return_train_score=True,
                              verbose=2)

model_rf.fit(x_train,y)
best_model = model_rf.best_estimator_

joblib.dump (model_rf, './cross_validation.joblib', compress=3)
joblib.dump (best_model, './best_model.joblib', compress=3)

print (model_rf.best_params_)
roc_auc = my_roc_auc_score (best_model, x_val, y_val)
cross_val = cross_val_score (best_model, x_val, y_val, cv=5, scoring='roc_auc')
print ('roc_auc', roc_auc)
print ('cross val', cross_val)
print ('score', best_model.score (x_val, y_val))


df_cv_results = pd.DataFrame(model_rf.cv_results_)
df_cv_results = df_cv_results[['rank_test_score','mean_test_score','mean_train_score',
                           'param_n_estimators', 'param_min_samples_split','param_min_samples_leaf',
                           'param_max_features', 'param_max_depth','param_criterion']]
df_cv_results.sort_values('rank_test_score', inplace=True)
print (df_cv_results[:20])
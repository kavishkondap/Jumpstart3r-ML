import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import PartialDependenceDisplay
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest, f_regression

from sklearn.model_selection import RandomizedSearchCV, GridSearchCV


# Set the style
# plt.style.use('fivethirtyeight')

data = pd.read_excel('machineLearningData14.xlsx')
labels = np.array(data.pop('successes'))

# Data not being used for ML model
data.pop("ids")
data.pop("urls")
data.pop('locations')
data.pop ('title_keywords')
data.pop ('blurb_keywords')
titles = data.pop("titles")
blurbs = data.pop("blurbs")

data['media']-=1

X, x_val, y, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)
# var_columns = [c for c in data]
# print(var_columns)

# # Number of trees in random forest
# n_estimators = [int(x) for x in np.linspace(start = 10, stop = 200, num = 10)]
# # Number of features to consider at every split
# max_features = ['auto', 'sqrt']
# # Maximum number of levels in tree
# max_depth = [int(x) for x in np.linspace(30, 70, num = 5)]
# max_depth.append(None)
# # Minimum number of samples required to split a node
# min_samples_split = [12, 14, 16, 18]
# # Minimum number of samples required at each leaf node
# min_samples_leaf = [1, 2]
# # Method of selecting samples for training each tree
# bootstrap = [True, False]
# random_grid = {'n_estimators': n_estimators,
#                'max_depth': max_depth,
#                'min_samples_split': min_samples_split,
#                'min_samples_leaf': min_samples_leaf,
#                'bootstrap': bootstrap}

# model_rf = RandomForestClassifier()

# rf_random = RandomizedSearchCV (estimator=model_rf, param_distributions=random_grid, n_iter=100, cv=3, verbose = 2, random_state=42, n_jobs=-1)
# rf_random.fit (X, y)
# print (rf_random.best_params_)

# print ('improved', rf_random.best_estimator_.score (x_val, y_val))

param_grid = {
    'bootstrap': [True],
    'max_depth': [70],
    'min_samples_leaf': [0.001, 0.01, 0.1, 0.5, 1],
    'min_samples_split': [9],
    'n_estimators': [1600]
}

rf_grid = RandomForestClassifier()
grid_search = GridSearchCV (estimator=rf_grid, param_grid=param_grid, cv=3, n_jobs = -1, verbose = 2)
grid_search.fit (X, y)
print ('best grid', grid_search.best_params_)
print ('best grid accuracy', grid_search.best_estimator_.score (x_val, y_val))

# exit()
# class_weight='balanced',
#                                   criterion='gini',
#                                   max_depth=None,
#                                   max_features='log2',
#                                   min_samples_leaf=0.005,
#                                   min_samples_split=0.015,
#                                   n_estimators=100
model_rf = RandomForestClassifier()
model_rf.fit(X, y)
print (model_rf.feature_importances_)

print ('score', model_rf.score (x_val, y_val))


exit()


df_var_imp = pd.DataFrame({'Variable': var_columns,
                           'Importance': model_rf.feature_importances_}) \
                .sort_values(by='Importance', ascending=False) \
                .reset_index(drop=True)

# Customize the bar plot
fig, ax = plt.subplots(figsize=(10, 6))
df_var_imp[:13].sort_values('Importance').plot('Variable', 'Importance', 'bar', color='lightgreen', legend=False, ax=ax)
ax.set_title('Feature Importance')
ax.set_xlabel('Relative Importance')
ax.set_ylabel('Variable')

# Rotate x-axis labels and adjust figure size for wrapped text
plt.xticks(rotation=0, ha='center', wrap=True)
fig.tight_layout()

plt.show()

# Customize the partial dependence plot
fig, ax = plt.subplots(figsize=(12, 6))
# display = PartialDependenceDisplay.from_estimator(model_rf, X, features=['updates', 'comments', 'blurbs_length', 'converted_goals', 'category_success_rate', 'num_creation_days', 'num_days', 'media', 'titles_num_cap', 'latitudes', 'titles_length', 'longitudes', 'blurb_sentiment', 'blurbs_num_cap', 'blurbs_num_num', 'fx_rate', 'title_sentiment', 'blurbs_num_exc', 'title_keywords', 'titles_num_exc'])
display = PartialDependenceDisplay.from_estimator(model_rf, X, features=['updates', 'comments', 'blurbs_length', 'converted_goals', 'category_success_rate', 'num_creation_days', 'num_days'])
display.plot(ax=ax)
ax.set_title('Partial Dependence')
ax.set_xlabel('Feature Value')
ax.set_ylabel('Partial Dependence')
# plt.tight_layout()
plt.show()
# display.plot(ax=ax)
# plt.show()
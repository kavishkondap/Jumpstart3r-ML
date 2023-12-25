import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import PartialDependenceDisplay
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import textwrap

def wrap_labels (ax, width, break_long_words = False):
    labels = []
    for label in ax.get_xticklabels ():
        text = label.get_text()
        labels.append (textwrap.fill (text, width=width, break_long_words=break_long_words))
    ax.set_xticklabels (labels, rotation = 0)

# Set the style
# plt.style.use('fivethirtyeight')

data = pd.read_excel('machineLearningData14_1.xlsx')
labels = np.array(data.pop('successes'))

# Data not being used for ML model
data.pop("ids")
data.pop("urls")
data.pop('locations')
titles = data.pop("titles")
blurbs = data.pop("blurbs")

data ['Number of Updates'] = data []

X, x_val, y, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)
var_columns = [c for c in data]
print(var_columns)

model_rf = RandomForestClassifier(class_weight='balanced',
                                  criterion='entropy',
                                  max_depth=None,
                                  max_features='log2',
                                  min_samples_leaf=0.005,
                                  min_samples_split=0.015,
                                  n_estimators=110)
model_rf.fit(X, y)
print (model_rf.feature_importances_)

df_var_imp = pd.DataFrame({'Variable': var_columns,
                           'Importance': model_rf.feature_importances_}) \
                .sort_values(by='Importance', ascending=False) \
                .reset_index(drop=True)

# Customize the bar plot
# fig, ax = plt.subplots()#figsize=(10, 6)
# df_var_imp[:10].sort_values('Importance').plot('Variable', 'Importance', 'bar', color='lightgreen', legend=False, ax=ax)
# ax.set_title('Feature Importance', fontdict={'fontsize': 'xx-large', 'fontweight': 'medium'})
# ax.set_xlabel('Variable')
# ax.set_ylabel('Relative Importance')
# ax.xaxis.label.set_fontsize ('x-large')
# ax.yaxis.label.set_fontsize ('x-large')
# wrap_labels (ax, 15)
# plt.show()

# Customize the partial dependence plot
fig, ax = plt.subplots()#figsize=(12, 6)
# display = PartialDependenceDisplay.from_estimator(model_rf, X, features=['updates', 'comments', 'blurbs_length', 'converted_goals', 'category_success_rate', 'num_creation_days', 'num_days', 'media', 'titles_num_cap', 'latitudes', 'titles_length', 'longitudes', 'blurb_sentiment', 'blurbs_num_cap', 'blurbs_num_num', 'fx_rate', 'title_sentiment', 'blurbs_num_exc', 'title_keywords', 'titles_num_exc'])
# display = PartialDependenceDisplay.from_estimator(model_rf, X, features=['updates', 'comments', 'blurbs_length', 'converted_goals', 'category_success_rate', 'num_creation_days', 'num_days'])
display = PartialDependenceDisplay.from_estimator(model_rf, X, features=['Number of Updates'])
display.plot(ax=ax)
ax.set_title('Partial Dependence')
ax.set_xlabel('Feature Value')
ax.set_ylabel('Partial Dependence')
# plt.tight_layout()
plt.show()
# display.plot(ax=ax)
# plt.show()

fig,ax = plt.subplots(1, 3, figsize=(18, 4))
X['Number of Updates'].hist(ax=ax[0], legend=True)
X['Number of Comments'].hist(ax=ax[1], legend=True)
X['Description Character Count'].hist(ax=ax[2], legend=True)
plt.show()
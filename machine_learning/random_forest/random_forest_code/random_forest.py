import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import PartialDependenceDisplay, partial_dependence
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

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

data['Media Type'] -= 1

X, x_val, y, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)
var_columns = [c for c in data]

model_rf = RandomForestClassifier()
model_rf.fit(X, y)
print(model_rf.feature_importances_)

print('score', model_rf.score(x_val, y_val))

#Feature Importances
df_var_imp = pd.DataFrame({'Variable': var_columns, 'Importance': model_rf.feature_importances_}).sort_values(by='Importance', ascending=False).reset_index(drop=True)

# Customize the bar plot
fig, ax = plt.subplots(figsize=(20, 12))
sorted = df_var_imp.sort_values('Importance')
hbars = ax.barh(list(sorted['Variable']), list(sorted['Importance']))
ax.set_xlabel('Relative Importance', fontname='Times New Roman', fontsize=15)
ax.set_ylabel('Variable', fontname='Times New Roman', fontsize=15)
vals = list(df_var_imp.sort_values('Importance')['Importance'])
print(vals)
print(type(hbars))
ax.bar_label(hbars, fmt='%.4f', fontname='Times New Roman', fontsize=15)
plt.yticks(rotation='horizontal', wrap=True, fontname='Times New Roman', fontsize=12)
plt.xscale('log')
plt.tick_params(axis='x', which='minor')
plt.xticks(fontname='Times New Roman', fontsize=15)

plt.show()
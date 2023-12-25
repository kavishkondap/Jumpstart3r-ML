import pandas as pd
import numpy as np

data = pd.read_excel ('machineLearningData14.xlsx')

labels = np.array(data.pop('successes'))

ids = data.pop("ids")
urls = data.pop("urls")
locations = data.pop('locations')
fx_rate = data.pop ('fx_rate')
category_success = data.pop ('category_success_rate')
titles = data.pop("titles")
blurbs = data.pop("blurbs")


q1s = []
q3s = []
iqrs = []
mins = []
maxes = []
stds = []
means = []

for key in data.keys ():
    q1s.append (np.percentile (data[key], 25, method='midpoint'))
    q3s.append (np.percentile (data[key], 75, method='midpoint'))
    iqrs.append (q3s[-1]-q1s[-1])
    
    maxes.append (q3s[-1]+1.5*iqrs[-1])
    mins.append (q1s[-1]-1.5*iqrs[-1])
    stds.append (np.std (data[key]))
    means.append (np.mean (data[key]))


print ('keys', data.keys())
print ('mins', mins)
print ('maxes', maxes)
print ('q1', q1s)
print ('q3s', q3s)
print ('iqrs', iqrs)
print ('means', means)
print ('stds', stds)
print (data[data.keys()[0]][0])
indicies_to_remove = []
count = 0

threshold = 3

for i in range (len (data['updates'])):
    for j, attr in enumerate (list (data.keys ())):
        if np.abs ((data[attr][i]-means[j])/stds[j])>threshold:
            indicies_to_remove.append (i)
            # print ('removed', i)
            count+=1
            break


# labels = np.array(data.pop('successes'))

# ids = data.pop("ids")
# urls = data.pop("urls")
# locations = data.pop('locations')
# fx_rate = data.pop ('fx_rate')
# category_success = data.pop ('category_success_rate')
# titles = data.pop("titles")
# blurbs = data.pop("blurbs")

data ['successes'] = labels
data ['ids'] = ids
data ['urls'] = urls
data ['locations'] = locations
data ['fx_rate'] = fx_rate
data ['category_success_rate'] = category_success
data ['titles'] = titles
data ['blurbs'] = blurbs

print (count)
indicies_to_remove = list (set (indicies_to_remove))
print (indicies_to_remove)
print (len (indicies_to_remove))
data.drop (indicies_to_remove, inplace=True)
# print (len (df2['updates']))
# print (len (df2['titles']))
# print (np.array (df2).shape)
data.to_csv ('machineLearningData18.csv')
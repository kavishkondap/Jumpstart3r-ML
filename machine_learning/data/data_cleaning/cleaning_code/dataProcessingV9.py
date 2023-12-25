import pandas as pd
import numpy as np

data = pd.read_excel ('machineLearningData8.xlsx')

old_data = pd.read_excel ('KickstarterData.xlsx')
old_titles = old_data ['title']
old_locations = old_data ['location']
old_locations = old_locations.str.strip ().str.replace ('\n', '')
# print (old_locations)
# id_to_location = {}
# for i in range (len (old_ids)):
#     id_to_location [old_ids[i]] = old_locations[i]
#     # print (id_to_location)

titles = data ['titles']
blurbs = data ['blurbs']
ids = data ['ids']

# print (type (old_ids[i]))
# print (ids)
# print (titles)

# for i in range (len (old_titles)):
#     print (old_titles[i])
#     if (old_titles[i] in titles):
#         locations.append (old_locations[i])
#         print ('found')

# data ['locations'] = locations
# data.to_excel ('machineLearningData7.xlsx')

# keywords = {
#     ''
# }

curr_id = data ['ids']
old_id = old_data ['id']

id_to_location = {}
for i in range (len (old_id)):
    if (type (old_locations[i])==str):
        old_locations [i] = old_locations[i].replace (',', '')
        # print (old_locations[i])
    id_to_location [old_id[i]] = old_locations[i]
    # print (id_to_location)

locations = []
total_wrong = 0
count = 0
for id in curr_id:
    locations.append (id_to_location[id])
    count+=1
    print (count)


data ['locations'] = locations
data.to_excel ('machineLearningData9.xlsx', index = False)
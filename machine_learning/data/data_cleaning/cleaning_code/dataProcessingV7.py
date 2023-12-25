import pandas as pd
import numpy as np

data = pd.read_excel ('machineLearningData6.xlsx')

old_data = pd.read_excel ('KickstarterData.xlsx')
old_titles = old_data ['title']
old_comments = old_data ['comment']
old_comments = old_comments.str.strip ().str.replace ('\n', '')
# print (old_comments)
# id_to_comment = {}
# for i in range (len (old_ids)):
#     id_to_comment [old_ids[i]] = old_comments[i]
#     # print (id_to_comment)

titles = data ['titles']
blurbs = data ['blurbs']
ids = data ['ids']

# print (type (old_ids[i]))
# print (ids)
# print (titles)

# for i in range (len (old_titles)):
#     print (old_titles[i])
#     if (old_titles[i] in titles):
#         comments.append (old_comments[i])
#         print ('found')

# data ['comments'] = comments
# data.to_excel ('machineLearningData7.xlsx')

# keywords = {
#     ''
# }

curr_id = data ['ids']
old_id = old_data ['id']

id_to_comment = {}
for i in range (len (old_id)):
    if (type (old_comments[i])==str):
        old_comments [i] = old_comments[i].replace (',', '')
        # print (old_comments[i])
    id_to_comment [old_id[i]] = old_comments[i]
    # print (id_to_comment)

comments = []
total_wrong = 0
for id in curr_id:
    comments.append (id_to_comment[id])
    # try:
    #     if ((id_to_comment[id]).isnumeric()):
    #         comments.append (id_to_comment[id])
    #     else:
    #         print (id, id_to_comment[id])
    #         print ('failure')
    #         exit()
    #     # print (id_to_comment[id], len (comments))
    # except:
    #     print (id, id_to_comment[id])


# data ['comments'] = comments
# data.to_excel ('machineLearningData7.xlsx', index = False)
import pandas as pd

def getDays (data, index):
    seconds = data['launched_at'][index]-data['created_at'][index]
    days = seconds/86400
    return days

data = dict (pd.read_excel ('machineLearningData3.xlsx'))
other_data = pd.read_csv ('OtherData.csv')
creation_time = []
valid_ids = []
for i in range (len (other_data['id'])):
    # for id in data['ids']:
    # print (type (other_data['id'][i]))
    # print (type (data['ids'][i]))
    # print (type (data['titles']))
        # print ('hit')
    if (other_data['id'][i] in list (data['ids'])):
        valid_ids.append (other_data['id'][i])
        # print ("hit", len (creation_time))
        creation_time.append (getDays (other_data, i))
print (len (valid_ids))
print (len (list(set(valid_ids))))
data ['creation_time'] = creation_time
print (len (creation_time))
df = pd.DataFrame (data, columns=['ids', 'urls', 'successes', 'titles', 'blurbs', 'converted_goals', 'fx_rate', 'top_media', 'bottom_media', 'category_success_rate', 'num_days', 'updates', 'title_length', 'title_num_cap', 'title_num_num', 'title_num_exc', 'blurbs_length', 'blurbs_num_cap', 'blurbs_num_num', 'blurbs_num_exc', 'creation_time'])
df.to_excel ('machineLearningData4.xlsx')
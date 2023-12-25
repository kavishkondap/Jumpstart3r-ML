import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import re
from currency_conversions import curr_converter

raw_data = pd.read_excel ('combinedData.xlsx')

def check_validity (data, index):
    check_validity = True
    columns = ['id_collected', "urls_collected","success_collected", "title_collected", "blurb_collected", "update_collected", "topvideo_collected",  "topimage_collected", "bottomvideo_collected", "bottomimage_collected", 'Category', 'Type', 'deadline', 'fx_rate', 'goal', 'launched_at', 'state']
    if not (data ['state'][index]=='failed' or data ['state'][index]=='successful'):
        check_validity=False
    for column in columns:
        if (data[column][index]==None or pd.isnull (data.loc [index, column]) or 'UNUSUAL WEBSITE' in str (data[column][index]) or "PRIVATE WEBSITE" in str (data[column][index])):
            check_validity=False
    # print (index, check_validity)
    return check_validity

def getTopMedia (data, index):
    if (data['topvideo_collected'][index]):
        return 2
    if (data['topimage_collected'][index]):
        return 1
    return 0

def getBottomMedia (data, index):
    if (data['bottomvideo_collected'][index]):
        return 2
    if (data['bottomimage_collected'][index]):
        return 1
    return 0

def getDays (data, index):
    seconds = data['deadline'][index]-data['launched_at'][index]
    days = int (seconds/86400)
    return days

# Eliminate a website if:
# Not successful/failure (different state)
# UNUSUAL WEBSITE present in any of the cells
# Any cell is blank

trimmed_data = {
    'ids':[],
    'urls':[],
    'titles':[],
    'successes':[],
    'blurbs':[],
    'converted_goals':[],
    'fx_rate':[],
    'top_media':[],
    'bottom_media':[],
    'category_success_rate':[],
    'num_days':[],
    'updates':[],
}

success_rate = {
    'Games':46.69,
    'Design':41.62,
    "Technology":22.45,
    "Film & Video":38.09,
    "Video":38.09,
    "Publishing":36.54,
    "Music":50.38,
    "Fashion":30.60,
    "Food":26.01,
    "Comics":64.82,
    "Art":48.00,
    "Photography":34.53,
    "Theater":59.96,
    "Crafts":26.91,
    "Journalism":23.34,
    "Dance":61.48,
}

num_invalid = 0
for i in range (len (raw_data['id_collected'])):
    if (check_validity (raw_data, i)):
        try:
            trimmed_data['ids'].append (int (raw_data['id_collected'][i]))
            trimmed_data['urls'].append (str (raw_data['urls_collected'][i]))
            trimmed_data['titles'].append (len (str (raw_data['title_collected'][i])))
            trimmed_data ['successes'].append (int (raw_data['success_collected'][i]))
            trimmed_data['blurbs'].append (len (str (raw_data['blurb_collected'][i])))
            trimmed_data['converted_goals'].append (float (raw_data['goal'][i]*raw_data['fx_rate'][i]))
            trimmed_data['fx_rate'].append (float (raw_data['fx_rate'][i]))
            trimmed_data ['top_media'].append (getTopMedia (raw_data, i))
            trimmed_data['bottom_media'].append (getBottomMedia (raw_data, i))
            trimmed_data['category_success_rate'].append (float (success_rate [str (raw_data['Type'][i])[12:]]))
            trimmed_data['num_days'].append (getDays (raw_data, i))
            trimmed_data['updates'].append (int (raw_data ['update_collected'][i]))
        # trimmed_data []
            # print (i)
            # print (type (raw_data ['topvideo_collected'][i]))
            # print (type (raw_data ['topimage_collected'][i]))
            # print (type (raw_data ['bottomvideo_collected'][i]))
            # print (type (raw_data ['bottomimage_collected'][i]))
        except:
        #     # pass
        #     num_invalid+=1
            print (i, raw_data['Type'][i], raw_data['title_collected'][i])
    
        # print (i, raw_data['title_collected'][i])
# print (num_invalid)

df = pd.DataFrame (trimmed_data, columns= ['ids',
    'urls',
    'titles',
    'successes',
    'blurbs',
    'converted_goals',
    'fx_rate',
    'top_media',
    'bottom_media',
    'category_success_rate',
    'num_days',
    'updates',])
df.to_excel ('machineLearningData2.xlsx')
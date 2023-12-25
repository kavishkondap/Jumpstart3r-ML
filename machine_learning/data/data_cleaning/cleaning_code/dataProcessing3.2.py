import pandas as pd
def numCapitals (input):
    numCapitals = 0
    for i in range (len (input)):
        if (input[i].isupper()):
            numCapitals+=1
    return numCapitals
def numNums (input):
    numNum = 0
    for i in range (len (input)):
        if (input[i].isnumeric ()):
            numNum+=1
    return numNum
def numExc (input):
    numExc = 0
    for i in range (len (input)):
        if (input[i]=='!'):
            numExc+=1
    return numExc

data = dict (pd.read_excel ('machineLearningData.xlsx'))
titles = data['titles']
blurbs = data['blurbs']
titles_length = []
blurbs_length = []
titles_num_cap = []
blurbs_num_cap = []
titles_num_num = []
blurbs_num_num = []
titles_num_exc = []
blurbs_num_exc = []
for title in titles:
    titles_length.append (len (title))
    titles_num_cap.append (numCapitals(title))
    titles_num_num.append (numNums (title))
    titles_num_exc.append (numExc (title))
for blurb in blurbs:
    blurbs_length.append (len (blurb))
    blurbs_num_cap.append (numCapitals (blurb))
    blurbs_num_num.append (numNums (blurb))
    blurbs_num_exc.append (numExc (blurb))
data ['title_length'] = titles_length
data ['title_num_cap'] = titles_num_cap
data ['title_num_num'] = titles_num_num
data ['title_num_exc'] = titles_num_exc

data ['blurbs_length'] = blurbs_length
data ['blurbs_num_cap'] = blurbs_num_cap
data ['blurbs_num_num'] = blurbs_num_num
data ['blurbs_num_exc'] = blurbs_num_exc

df = pd.DataFrame (data, columns=['ids', 'urls', 'successes', 'titles', 'blurbs', 'converted_goals', 'fx_rate', 'top_media', 'bottom_media', 'category_success_rate', 'num_days', 'updates', 'title_length', 'title_num_cap', 'title_num_num', 'title_num_exc', 'blurbs_length', 'blurbs_num_cap', 'blurbs_num_num', 'blurbs_num_exc'])
df.to_excel ('machineLearningData3.xlsx')
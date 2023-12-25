import pandas as pd
import numpy as np

data = pd.read_excel ('machineLearningData7.xlsx')
titles = data ['titles']
blurbs = data ['blurbs']

# title_keywords = {
#     'free shipping': [],
#     'you recieve': [],
#     'early bird': [],
#     'be the first': [],
#     'your reward': [],
#     'friends': [],
#     'friendship': [],
#     'community': [],
#     'family': [],
#     'people': [],
#     'passion': [],
#     'dream': [],
#     'inspired to start': [],
#     'believe that': [],
#     'impact': [],
#     'volunteer': [],
#     'thank you': [],
#     'so thankful': [],
#     'thanks': [],
#     'thanks so much': [],
#     'grateful': [],
#     'why support': [],
#     'funds will cover': [],
#     'will be used': [],
#     'aiming to': [],
#     'aim to raise': [],
#     'help us': [],
#     'we can': [],
#     'we raise': [],
#     'we plan to': [],
#     'we need': [],
#     'we found': [],
#     'we created': [],
#     'private': [],
#     'early bird': [],
#     'cds': [],
#     'pdf': [],
#     'stretch': [],
#     'shipping': [],
#     'print': [],
#     'retail': [],
#     'invitation': [],
#     'edition': [],
#     'unlocked': [],
#     "we'll": [],
#     'download': [],
#     'personalized': [],
#     'autograph': [],
#     'thank email': [],
#     'app': [],
#     'free': [],
#     'shirt': [],
#     'product': [],
#     'hand signed': [],
#     'logo': [],
#     "i'll": [],
#     'shoutout video': [],
#     'poster': [],
#     'coffee mug': [],
#     'hat': [],
#     'named': [],
# }

# blurbs_keywords = {
#     'free shipping': [],
#     'you recieve': [],
#     'early bird': [],
#     'be the first': [],
#     'your reward': [],
#     'friends': [],
#     'friendship': [],
#     'community': [],
#     'family': [],
#     'people': [],
#     'passion': [],
#     'dream': [],
#     'inspired to start': [],
#     'believe that': [],
#     'impact': [],
#     'volunteer': [],
#     'thank you': [],
#     'so thankful': [],
#     'thanks': [],
#     'thanks so much': [],
#     'grateful': [],
#     'why support': [],
#     'funds will cover': [],
#     'will be used': [],
#     'aiming to': [],
#     'aim to raise': [],
#     'help us': [],
#     'we can': [],
#     'we raise': [],
#     'we plan to': [],
#     'we need': [],
#     'we found': [],
#     'we created': [],
#     'private': [],
#     'early bird': [],
#     'cds': [],
#     'pdf': [],
#     'stretch': [],
#     'shipping': [],
#     'print': [],
#     'retail': [],
#     'invitation': [],
#     'edition': [],
#     'unlocked': [],
#     "we'll": [],
#     'download': [],
#     'personalized': [],
#     'autograph': [],
#     'thank email': [],
#     'app': [],
#     'free': [],
#     'shirt': [],
#     'product': [],
#     'hand signed': [],
#     'logo': [],
#     "i'll": [],
#     'shoutout video': [],
#     'poster': [],
#     'coffee mug': [],
#     'hat': [],
#     'named': [],
# }

pos_keywords = ['free shipping',
    'you recieve',
    'early bird',
    'be the first',
    'your reward',
    'friends',
    'friendship',
    'community',
    'family',
    'people',
    'passion',
    'dream',
    'inspired to start',
    'believe that',
    'impact',
    'volunteer',
    'thank you',
    'so thankful',
    'thanks',
    'thanks so much',
    'grateful',
    'why support',
    'funds will cover',
    'will be used',
    'aiming to',
    'aim to raise',
    'help us',
    'we can',
    'we raise',
    'we plan to',
    'we need',
    'we found',
    'we created',
    'private',
    'early bird',
    'cds',
    'pdf',
    'stretch',
    'shipping',
    'print',
    'retail',
    'invitation',
    'edition',
    'unlocked',
    "we'll",
    'download',
    'personalized',
    ]

neg_keywords = ['autograph',
    'thank email',
    'app',
    'free',
    'shirt',
    'product',
    'hand signed',
    'logo',
    "i'll",
    'shoutout video',
    'poster',
    'coffee mug',
    'hat',
    'named']
pos_keyword_title_count = []
pos_keyword_blurb_count = []
neg_keyword_title_count = []
neg_keyword_blurb_count = []


for title in titles:
    title = title.lower ()
    pos_count = 0
    for keyword in pos_keywords:
        if (keyword in title):
            pos_count+=1
    print (title, pos_count)
    pos_keyword_title_count.append (pos_count)
    neg_count = 0
    for keyword in neg_keywords:
        if (keyword in title):
            neg_count+=1
    neg_keyword_title_count.append (neg_count)

for blurb in blurbs:
    blurb = blurb.lower ()
    pos_count = 0
    for keyword in pos_keywords:
        if (keyword in blurb):
            pos_count+=1
    print (blurb, pos_count)
    pos_keyword_blurb_count.append (pos_count)
    neg_count = 0
    for keyword in neg_keywords:
        if (keyword in blurb):
            neg_count+=1
    neg_keyword_blurb_count.append (neg_count)
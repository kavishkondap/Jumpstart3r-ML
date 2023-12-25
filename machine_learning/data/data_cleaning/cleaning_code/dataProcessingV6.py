import pandas as pd

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def quantify_sentiment(phrase):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(phrase)
    
    # The sentiment scores range from -1 to +1
    # Positive scores indicate positive sentiment, negative scores indicate negative sentiment
    # The compound score is a normalized score combining the other scores
    positive_score = sentiment_scores['pos']
    negative_score = sentiment_scores['neg']
    compound_score = sentiment_scores['compound']
    
    return positive_score, negative_score, compound_score

data = pd.read_excel ('machineLearningData5.xlsx')

titles = data['titles']
blurbs = data ['blurbs']

title_sentiment = []
blurbs_sentiment = []

for i in range (len (titles)):
    positive_score_title, negative_score_title, compound_score_title = quantify_sentiment(titles[i])
    title_sentiment.append (compound_score_title)
    # print ('title', compound_score_title)
    positive_score_blurb, negative_score_blurb, compound_score_blurb = quantify_sentiment(blurbs[i])
    blurbs_sentiment.append (compound_score_blurb)
    # print ('blurb', compound_score_blurb)
    if i % 100 ==0:
        print (i)

print (title_sentiment)
print (blurbs_sentiment)
data ['title_sentiment'] = title_sentiment
data ['blurb_sentiment'] = blurbs_sentiment

data.to_excel ('machineLearningData6.xlsx')

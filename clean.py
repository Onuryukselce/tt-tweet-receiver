# utilities
import re
import pickle
import os
import string
import numpy as np
import pandas as pd
# plotting
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# nltk
from nltk.stem import WordNetLemmatizer
#sklearn
from sklearn.feature_extraction.text import CountVectorizer

""" os.chdir(os.getcwd())
print(os.getcwd()) """
# Importing the dataset
DATASET_ENCODING = "ISO-8859-1"
DATASET_COLUMNS = ['id', 'created_at', 'tweet_translated']
df = pd.read_csv('./translated_tweets.csv', encoding=DATASET_ENCODING, usecols=DATASET_COLUMNS)
tweet_ids = df['id']
tweet_dates = df['created_at']
tweets = df['tweet_translated']

print(df.keys())





def text_clean(text):
    text = text_lowercase(text)
    text = text_delete_at_character(text)
    text = text_delete_hashtags(text)
    text = text_delete_rt_word(text)
    text = text_delete_quotation_marks(text)
    text = text_delete_punctuation(text)
    text= text_delete_enter_character(text)
    text = text_delete_words_that_contain_numbers(text)
    text = text_delete_double_or_more_spaces(text)
    text = text_trim(text)
    return text


def text_lowercase(text):
    return text.lower()

def text_delete_punctuation(text):
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    return text

def text_delete_words_that_contain_numbers(text):
    text = re.sub('\w*\d\w*', '', text)
    return text
def text_delete_quotation_marks(text):
    text = re.sub('[?????]', '', text)
    return text

def text_delete_enter_character(text):
    text = re.sub('\n', '', text)
    return text

def text_delete_hashtags(text):
    text = re.sub('(#\S+)|(#\s+\S+)', '', text)
    return text

def text_delete_at_character(text):
    text = re.sub('(@\S+)|(#\s+\S+)', '', text)
    return text

def text_delete_rt_word(text):
    text = re.sub('(\s+rt\s+)|(^rt\s+)', ' ', text)
    return text

def text_delete_double_or_more_spaces(text):
    text = re.sub('\s\s+', ' ', text)
    return text

def text_trim(text):
    text = text.strip()
    return text

cleaned_tweets = lambda x: text_clean(x)




tweet_clean = pd.DataFrame(df.tweet_translated.apply(cleaned_tweets))
tweet_clean.to_pickle('./data/clean_translated_tweets.pkl')

cv = CountVectorizer(stop_words='english')
tweet_cv = cv.fit_transform(tweet_clean.tweet_translated)
tweet_dtm = pd.DataFrame(tweet_cv.toarray(), columns=cv.get_feature_names_out())
tweet_dtm.index = tweet_clean.index
print(tweet_dtm)


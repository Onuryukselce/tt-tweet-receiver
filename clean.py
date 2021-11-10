# -*- coding: latin-1 -*-


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
#zemberek morph analyzer
from zemberek import TurkishMorphology

""" os.chdir(os.getcwd())
print(os.getcwd()) """
# Importing the dataset
DATASET_ENCODING = "UTF-8"
DATASET_COLUMNS = ['id', 'created_at', 'tweet','tweet_translated']
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


##cleaning the translated tweets and saving them

cleaned_translated_tweets = lambda x: text_clean(x)



tweet_translated_clean = pd.DataFrame(df.tweet_translated.apply(cleaned_translated_tweets))

cv = CountVectorizer(stop_words='english')
translated_tweet_cv = cv.fit_transform(tweet_translated_clean.tweet_translated)
translated_tweet_dtm = pd.DataFrame(translated_tweet_cv.toarray(), columns=cv.get_feature_names_out())
translated_tweet_dtm.index = tweet_translated_clean.index
""" print(translated_tweet_dtm) """

translated_tweet_dtm.to_pickle("./data/translated_tweet_dtm.pkl")
tweet_translated_clean.to_pickle("./data/tweet_clean_translated_aka_corpus.pkl")

##cleaning the native tweets and saving them
cleaned_tweets = lambda x: text_clean(x)
tweet_clean = pd.DataFrame(df.tweet.apply(cleaned_tweets))

stop_words_df=pd.read_csv('https://raw.githubusercontent.com/InJuxSanct/turkish-stopwords/master/src/lib/stopwords/raw-stopwords.txt', sep=" ", header=None)
stop_words_df.columns=['words_list']

#stop words cleaning
cv2 = CountVectorizer(stop_words=list(stop_words_df['words_list']))
tweet_cv = cv2.fit_transform(tweet_clean.tweet)

#lemmatization with zemberek
morphology = TurkishMorphology.create_with_defaults()
results = morphology.analyze("vakalar")
print(results)
for result in results:
    print(result)
    print("\n") 


""" for value in cv2.get_feature_names_out():
    results = morphology.analyze(value)
    for result in results:
        print(result)
        print("\n") """

""" tweet_dtm = pd.DataFrame(tweet_cv.toarray(), columns=cv2.get_feature_names_out())
tweet_dtm.index = tweet_clean.index
print(tweet_dtm)

tweet_dtm.to_pickle("./data/tweet_dtm.pkl")
tweet_clean.to_pickle("./data/tweet_clean_aka_corpus.pkl") """

# TODO:
## Zemberek, Zeyrek ve Diğer kütüphaneler ile lemmatization normalization işlemlerini gerçekleştir.
## dtm'yi çıkart.
# -*- coding:utf-8 -*-


# utilities
import re
import numpy as np
import pandas as pd
from collections import Counter
# plotting
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# nltk
from nltk.stem import WordNetLemmatizer
# sklearn
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report


# Importing the document term matrix
data = pd.read_pickle('./data/tweet_dtm.pkl')
data = data.transpose()
print(data.head())

# Find the top 15 words for each tweet
top_dict = {}
for c in data.columns:
    top = data[c].sort_values(ascending=False).head(15)
    top_dict[c]= list(zip(top.index, top.values))

top_dict

words = []
# get all words said by fahrettinkoca
for tweet in data.columns:
    top = [word for (word, count) in top_dict[tweet]]
    for t in top:
        words.append(t)

top_words = Counter(words).most_common()
print(top_words)
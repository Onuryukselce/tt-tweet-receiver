# utilities
import re
import numpy as np
import pandas as pd
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


# Importing the dataset
DATASET_ENCODING = "ISO-8859-1"
DATASET_COLUMNS = ['id', 'created_at', 'tweet']
df = pd.read_csv('./tmp/clean_and_sorted_tweets.csv', encoding=DATASET_ENCODING, usecols=DATASET_COLUMNS)
df.sample(5)
print(df.columns)
print('length of data is', len(df))
print(df.shape)
print(df.info)
print(df.dtypes)
print('null =>' + str(np.sum(df.isnull().any(axis=1))))
print('Count of columns in the data is:  ', len(df.columns))
print('Count of rows in the data is:  ', len(df))
print(df['tweet'].nunique())

# Plotting the distribution for dataset.
ax = df.groupby('id').count().plot(kind='bar', title='Distribution of data',legend=False)
ax.set_xticklabels(['Negative','Positive'], rotation=0)
# Storing data in lists.
text, sentiment = list(df['tweet']), list(df['id'])
plt.show()

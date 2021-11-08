import seeker
import pandas as pd
import twint


""" twitSearcher = seeker.Seeker()
twitSearcher.get_tweets_from_user_with_replies_by_date("drfahrettinkoca","20/02/2020","14/03/2020") """

""" twitSearcher = seeker.Seeker()
twitSearcher.get_all_timeline_of_user("drfahrettinkoca") """

import os
import glob
import pandas as pd


""" os.chdir('./tmp')
file_extension = ".csv"
file_starts_with = "drfahrettinkoca"


files = [i for i in glob.glob(f"{file_starts_with}*{file_extension}")]
files.append('timeline_data_of_drfahrettinkoca.csv')
combined_csv_data = pd.concat([pd.read_csv(f, delimiter=',', encoding='UTF-8',engine='python', error_bad_lines=False ) for f in files])
combined_csv_data.to_csv('combined_csv_data.csv')


df = pd.read_csv('combined_csv_data.csv')
df.drop_duplicates(subset="id",keep=False,inplace=True)
df.sort_values(by=['created_at'],inplace=True)
df.to_csv('clean_and_sorted_tweets.csv')
print(df) """

""" os.chdir('./tmp')
file_extension = ".csv"
file_starts_with = "replies_to_drfahrettinkoca"

files = [i for i in glob.glob(f"{file_starts_with}*{file_extension}")]
files.append('all_replies_to_drfahrettinkoca.csv')
combined_csv_data = pd.concat([pd.read_csv(f, delimiter=',', encoding='UTF-8',engine='python', error_bad_lines=False ) for f in files])
combined_csv_data.to_csv('combined_replies_csv_data.csv')

df = pd.read_csv('combined_replies_csv_data.csv')
df.drop_duplicates(subset="id",keep=False,inplace=True)
df.sort_values(by=['created_at'],inplace=True)
df.to_csv('clean_and_sorted_replies.csv')
print(df) """

import google_trans_new
from google_trans_new import google_translator
import time

translator = google_translator()
tweets = pd.read_csv('D:\\Twitter Sentiment Analysis Tesis\\twint-tweet-receiver-with-replies\\tmp\\clean_and_sorted_replies.csv')
tweets['tweet_translated'] = ""
print(tweets)
translated_tweets = []
for index,sentence in enumerate(tweets['tweet']):
    print(index, sentence)
    translate = True
    while translate == True:
        try:
            translation = translator.translate(sentence, lang_tgt='en', lang_src='tr')
            tweets.at[index, 'tweet_translated'] = translation
            translate = False
        except:
            time.sleep(30)
            print('30 Saniye bekleniyor, son ceviri '+ str(index) + " => " + sentence)
            translate = True

        



print(tweets)

""" translated_tweet_column = pd.DataFrame({'tweet_translated': translated_tweets})
print(translated_tweet_column)
tweets = pd.merge(tweets,translated_tweet_column, how='left') """
tweets.to_csv('translated_replies.csv')



""" from os import environ

from google.cloud import translate

project_id = environ.get("PROJECT_ID", "")
assert project_id
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient()

sample_text = "Hello world!"
target_language_code = "tr"

response = client.translate_text(
    contents=[sample_text],
    target_language_code=target_language_code,
    parent=parent,
)

for translation in response.translations:
    print(translation.translated_text) """






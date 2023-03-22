# Importing Required Packages
import tweepy
import pandas as pd
from datetime import datetime
import snscrape
import snscrape.modules.twitter as sntwitter
import json
import s3fs
import snscrape

def run_twitter_etl():

    # Created a list to append all Tweet Attributes(data)
    attributes_container = []


    # Extracting 2000 Tweets from Elon Musk's Twitter Account

    # Using TwitterSearchScraper to scrape data and Append Tweets to List
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:elonmusk').get_items()):
        if i>2000:
            break
        attributes_container.append([tweet.date, tweet.content])
        
    # Creating a dataframe from the Tweets listed above 
    tweets = pd.DataFrame(attributes_container, columns=["Date Created", "Tweets"])


    # Saving the DataFrame as a .csv file
    tweets.to_csv("s3://adwaith-airflow-twitter-etl/elonmusk_tweets.csv")

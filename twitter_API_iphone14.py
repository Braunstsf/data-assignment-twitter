
import os
import tweepy
from dotenv import load_dotenv

#getting the credentials from a .env file in my repository on Github: https://github.com/Braunstsf/hcd-data-assignment
consumer_key = os.environ["consumer_key"]
consumer_secret = os.environ["consumer_secret"]
access_token = os.environ["access_token"]
access_token_secret = os.environ["access_token_secret"]

auth = tweepy.OAuth1UserHandler(
  consumer_key, 
  consumer_secret, 
  access_token, 
  access_token_secret
)

api = tweepy.API(auth)

#trying to find a specific term that wouldn't be used for something else in context
tweets = api.search_tweets("iPhone 14", tweet_mode="extended")

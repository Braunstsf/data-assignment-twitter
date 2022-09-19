import tweepy
from tweepy import OAuthHandler
from tweepy import API
#from tweepy.streaming import StreamListener
from tweepy import Stream 
from tweepy import SListener

client = tweepy.Client(
	bearer_token="AAAAAAAAAAAAAAAAAAAAAE8IhQEAAAAA79D%2F2NQG%2FAnxDgn1%2Be9iui7ZYyg%3DzMZ2IT6zyHRZXObAipPQjmXMhPchFw6gl02MrNJKsZdNwSwJUY",
	consumer_key="c2zSjrnG0nUovYLBVWUpgbarv", 
	consumer_secret="Jz2LD9U0NRPbw50RykoUHeG58gGVkmslOUfJbEVHR3sAmuTwOQ",
	access_token="1337201030291812352-9qoUjlvFPfwbwpTeIRNtBK31koYGju",
	access_token_secret="HMqegjnsy6fQxGrLglUTh8oTc2PGQuzN3gLo9nkHeA20R"
	)
bearer_token="AAAAAAAAAAAAAAAAAAAAAE8IhQEAAAAA79D%2F2NQG%2FAnxDgn1%2Be9iui7ZYyg%3DzMZ2IT6zyHRZXObAipPQjmXMhPchFw6gl02MrNJKsZdNwSwJUY"
consumer_key="c2zSjrnG0nUovYLBVWUpgbarv"
consumer_secret="Jz2LD9U0NRPbw50RykoUHeG58gGVkmslOUfJbEVHR3sAmuTwOQ"
access_token="1337201030291812352-9qoUjlvFPfwbwpTeIRNtBK31koYGju"
access_token_secret="HMqegjnsy6fQxGrLglUTh8oTc2PGQuzN3gLo9nkHeA20R"

#OAuth Authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

#collecting stream data
listen = SListener(api)
stream = Stream(auth, listen)
stream.sample()

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')

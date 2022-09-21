import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "iPhone 14 until:2022-09-19 since:2022-09-06"
tweets = []
limit = 1000
for tweet in sntwitter.TwitterSearchScraper(query).get_items(): 
	if len(tweets) == limit:
		break
	else: 
		tweets.append([tweet.date,tweet.user.username, tweet.content, tweet.sourceUrl, tweet.lang, tweet.coordinates, tweet.user.location, tweet.likeCount, tweet.user.friendsCount, tweet.replyCount, tweet.retweetCount])

	#print(vars(tweet))
	#break
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'sourceUrl', 'Language', 'Coordinates', 'Location', 'Like Count', 'Friends', 'Replies', 'Retweets'])
print(df)

import tweepy
import tweepy_authentication

#getting the credentials from a .env file in my repository on Github: https://github.com/Braunstsf/hcd-data-assignment
client = tweepy.Client(bearer_token=tweepy_authentication.bearer_token)
query = 'iPhone OR iPhone 14' 
output = client.search_all_tweets(query=query, max_results=10, tweet_fields=['created_at', 'lang'], expansions=['author_id'])

users = {u['id']: u for u in output.includes['users']}

for tweet in output.data:
  if users[tweet.author_id]: 
     user = users[tweet.author_id]
     print(tweet.id)
     #print(user.username)
    # print(tweet.created_at)
     print(tweet.lang)
    # print(tweet.text)
   # print(tweet.lang)
    #print(tweet.created_at)
   

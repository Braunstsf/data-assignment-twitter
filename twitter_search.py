
import tweepy
import tweepy_authentication
import csv

#getting the credentials from a .env file in my repository on Github: https://github.com/Braunstsf/hcd-data-assignment
client = tweepy.Client(bearer_token=tweepy_authentication.bearer_token)
query = 'iPhone OR iPhone 14' 
output = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'lang', 'public_metrics'], expansions=['author_id'])

users = {u['id']: u for u in output.includes['users']}
#places = {u['id']: u for u in output.includes['places']}

headers = ['id', 'lang', 'username', 'created_at', 'public_metrics']
rows = []
for tweet in output.data:
  if users[tweet.author_id]: 
     user = users[tweet.author_id]
     rows.append(
      {'id': tweet.id,
      'lang': tweet.lang,
      'username': user.username,
      'created_at': tweet.created_at,
      'public_metrics':tweet.public_metrics}
      )
     '''
     print(tweet.id)
     print(tweet.lang)
     print(user.username)
     print(tweet.created_at)
     print(tweet.public_metrics)
     '''

with open('tweepy_data_iPhone.csv', 'w', encoding='UTF8', newline='') as f:
  writer = csv.DictWriter(f, fieldnames=headers)
  writer.writeheader()
  writer.writerows(rows)


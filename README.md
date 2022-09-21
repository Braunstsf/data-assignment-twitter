# hcd-data-assignment

The goal of the project was to find a relation on the retweets on a single tweet as well as the language that the tweet was written in. This resulted in three graphs/charts being created which are available as jpeg files in this repository. The first one shows the number of tweets written about the iPhone 14 in different languages, the second chart looks at the percentage of retweets on an individual tweet based on language with the third bar chart having the same data but displayed differently. 

The dataset was collected through Twitter API v2 and can be seen in my twitter_search.py file. I was able to find tweepy and endpoints from this documentation https://developer.twitter.com/en/docs/twitter-api. 

The source data was found by me through the code used to access Twitter API. 

There were 8 attributes in my data: ID, Language, Username, Created At, Retweets, Replies, Quotes, and Likes. 

ID - ID is the unique value of each twitter account.

Language - Languages in which the tweet were written in are put in this column.

username - Username represents the account's twitter username.

created_at - This represents the time that these tweets were created at

retweets - Retweets are the number of retweets the individual tweet got.

replies - The number of replies that an individual tweet received.

likes - It represents the number of likes a tweet received.

quotes - It represents the number of quote tweets made with the individual tweet.

There are no potential risks or biases seen in the data so far. It is some what non descriptive because of the Essential Account that I signed up for in the Twitter API.

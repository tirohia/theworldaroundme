import tweepy as tw
import access
import csv
import json

# creates a file with a dict of dicts - essentially a square matrix of [userId x userId]
# The file will be updated (not overwritten) periodically with new users


dd=dict()

with open('followed.csv', 'r') as f:
    reader = csv.reader(f)
    followed = next(reader)

d=dict(zip(followed, [0] * len(followed)))

for key,value in d.items():
    dd[key]=d

with open('usersFollowed.json','w') as f:
    f.write(json.dumps(dd))

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print tweet.text


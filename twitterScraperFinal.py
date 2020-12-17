import tweepy
import sys
import jsonpickle
import os

consumer_key = #KEY
consumer_secret = #KEY
access_token = #KEY
access_token_secret = #KEY

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

textfile = open('tweets.txt', 'w', encoding='utf-8')

maxTweets = 1000
tweetsPerQry = 100

sinceId = None

max_id = -1

tweetCount = 0

query = input('Enter query: ')

while tweetCount < maxTweets:
    try:
        if (max_id <= 0):
            if(not sinceId):
                new_tweets = api.search(q=query, count=tweetsPerQry)
            else:
                new_tweets = api.search(q=query, count=tweetsPerQry)
        else:
            if(not sinceId):
                new_tweets = api.search(q=query,count=tweetsPerQry, max_id=str(max_id - 1))
            else:
                new_tweets = api.search(q=query, count=tweetsPerQry, max_id=str(max_id - 1), since_id=sinceId)
        if not new_tweets:
            print("No more tweets found")
            break
        for tweet in new_tweets:
            #tweet = tweet.text.encode("utf-8")
            tweet = tweet.text
            textfile.write(str(tweet) + '\n')
        tweetCount += len(new_tweets)
        print('Downloaded {0} tweets'.format(tweetCount))
        max_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        print('some error: ' + str(e))
        break

print('Downloaded {0} tweets, Saved to {1}'.format(tweetCount, textfile.name))

textfile.close()

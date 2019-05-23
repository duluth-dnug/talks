import tweepy
import csv
import pandas as pd
from datetime import datetime


def authorizeTwitterApi():
    ####input your credentials here
    consumer_key = 'qXclhkhhayJXf88YiZO9q7UYA'
    consumer_secret = 'P65v5MzbyEWyqPafmyEpX4Xdrq8DCxySPsjK96vcmLTw4WbxNl'
    access_token = '3154969330-RR6EePv1mivDPqCyuYyWndaveodoTrFqxYaJ9T7'
    access_token_secret = 'PqYdFIZ4KvLBZ4fuj3DTPjKuZKBszSN1h6vQqAqYgpKGJ'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    return api

def getTweets(getCoordsOption, twitterApi, outfileName, searchTerm, lastId, geocodeExtent):
    csvFile = open(outfileName, 'wb') #wb=writes binary
    csvWriter = csv.writer(csvFile)

    headerRow = ['created_at', 'tweet_id', 'text', 'name', 'screen_name', 'language', 'lat', 'long']
    csvWriter.writerow(headerRow)
    for tweet in tweepy.Cursor(twitterApi.search,q=searchTerm,count=100000,
                            lang="en",
                            # since="2018-05-03",
                            since_id=lastId,
                            geocode=geocodeExtent
                            ).items():
        newRow = []
        if getCoordsOption == 'onlyspatial':
            if tweet.coordinates != None:
                newRow = [tweet.created_at, tweet.id, 
                            tweet.text.encode('utf-8'),
                            tweet.user.name.encode('utf-8'),
                            tweet.user.screen_name.encode('utf-8'),
                            tweet.user.lang,
                            tweet.coordinates['coordinates'][1],
                            tweet.coordinates['coordinates'][0]
                            ]  
        elif getCoordsOption == 'both':
            if tweet.coordinates != None:
                newRow = [tweet.created_at, 
                            tweet.id,
                            tweet.text.encode('utf-8'),
                            tweet.user.name.encode('utf-8'),
                            tweet.user.screen_name.encode('utf-8'),
                            tweet.user.lang,
                            tweet.coordinates['coordinates'][1],
                            tweet.coordinates['coordinates'][0]
                            ]          
            elif tweet.coordinates is None: 
                newRow = [tweet.created_at, 
                            tweet.id,
                            tweet.text.encode('utf-8'),
                            tweet.user.name.encode('utf-8'),
                            tweet.user.screen_name.encode('utf-8'),
                            tweet.user.lang
                            ]  
        elif getCoordsOption == 'nonspatial':
            newRow = [tweet.created_at, 
                        tweet.id,
                        tweet.text.encode('utf-8'),
                        tweet.user.name.encode('utf-8'),
                        tweet.user.screen_name.encode('utf-8'),
                        tweet.user.lang
                        ] 

        if len(newRow) > 2: print(newRow)
        csvWriter.writerow(newRow)    
    csvFile.close()


def main():
    formattedDate = datetime.now().strftime("%Y%m%d_%H%M")
    # usa = '39.8,-95.583068847656,2500km'   # this geocode includes nearly all American states (and a large portion of Canada)
    extentDesc = 'None'   
    extent = None 
    term = 'trail'
    lastTweetId = None

    csvFile = 'tweethistory_{0}_{1}_sinceID={2}_extent={3}.csv'.format(term, formattedDate, lastTweetId, extentDesc)
    
    getTweets(getCoordsOption='onlyspatial', 
                twitterApi=authorizeTwitterApi(), 
                outfileName=csvFile, 
                searchTerm=term, 
                lastId=lastTweetId, 
                geocodeExtent=extent)

if __name__ == "__main__":
    main()
import tweepy as tw

def getAuth():
    consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"
    access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx"

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tw.API(auth)
    print("setting up access ...")   
    return api


import tweepy
import access

api = access.getAuth()

class TSListener(tweepy.StreamListener):
    def on_status(self, status):
        get_user_informations(status)

    def on_error(self, status_code):
        if status_code == 403:
            print("Access refused. possibly rate limit reached")
            return False


def get_user_informations(tweet):
    print("User ID \t:" + str(tweet.user.id))
    print("User Name \t:" + tweet.user.name)
    print("User Screen name \t:" + tweet.user.screen_name)
    #print (tweet.entities.user_mentions[0])
    mentions = tweet.entities[u'user_mentions']
    if (bool(mentions)):
        for mention in mentions:
            print (mention)
            print (str(tweet.user.id) + "\t" + str(mentions[0][u'id']))


listener=TSListener()
myStream = tweepy.Stream(auth = api.auth, listener = listener)
print("streaming tweets ...")
myStream.userstream()


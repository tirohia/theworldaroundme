import tweepy
import access
import csv
import networkx as nx

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
            originating_user= tweet.user.id
            target_user = mentions[0][u'id']
            print ("tweeting at:\t"+ mentions[0][u'screen_name'])
            if originating_user in followed and target_user in followed:
                talkGraph.add_edge(orignating_user, target_user)
                nx.write_gml(talkGraph,"test.gml")
            components = nx.degree(talkGraph)
            for k, v in components.items():
                if v >= 1:
                    print (k,v)
            #for component in components:
            #    print (component)
			

### get list of people currently being followed
f=open("followed.csv",'r')
reader = csv.reader(f)
followed = next(reader)

#initialize graph
talkGraph=nx.Graph()
for user in followed:
    talkGraph.add_node(user)

listener=TSListener()
myStream = tweepy.Stream(auth = api.auth, listener = listener)
print("streaming tweets ...")
myStream.userstream()


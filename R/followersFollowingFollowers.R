
#   Build and Reload Package:  'Ctrl + Shift + B'
#   Check Package:             'Ctrl + Shift + E'
#   Test Package:              'Ctrl + Shift + T'

library("twitteR")
library("igraph")

## sets up setup_twitter_oauth
setwd("/home/ben/googleDrive/code/theworldaroundme/R")
source("access.R")
user<-getUser("3rdKingsland")
#following<-user$getFriends()
followers<-user$getFollowers()
connections<-data.frame(origin=user$name,destination=followers.df$name)

## The Sys.sleep is to get around twitter's request rate limiting.
for (user in followers){
  print(user)
  nextFollowers<-user$getFollowers()
  nextFollowers.df<-twListToDF(nextFollowers)
  userOverlap<-intersect(nextFollowers.df$name,userList)
  if (length(userOverlap)>0){
    connections <-rbind(connections,data.frame(origin=nextUser$name,destination=userOverlap))
  }
  Sys.sleep(10)
}

connections

g <- graph.data.frame(connections, directed = F)
V(g)$label <- V(g)$name
V(g)$size=3
V(g)$color="green"
tkplot(g)




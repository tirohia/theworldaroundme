import tweepy as tw
import csv
import time
import access

api = access.getAuth()

followed = list()

cursor = tw.Cursor(api.friends).items()

while True:
    try:
        friend = cursor.next()
        followed.append(friend.id)
        # Insert into db
    except tw.TweepError:
        time.sleep(60 * 15)
        continue
    except StopIteration:
        break

print (followed)


with open("followed.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(followed)
f.close()

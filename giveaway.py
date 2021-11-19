import tweepy
import random
from dotenv import load_dotenv
import os

load_dotenv()

TWITTER_APP_KEY = os.getenv('TWITTER_APP_KEY')
TWITTER_APP_SECRET = os.getenv('TWITTER_APP_SECRET')
TWITTER_KEY = os.getenv('TWITTER_KEY')
TWITTER_SECRET = os.getenv('TWITTER_SECRET')

auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)
api = tweepy.API(auth)

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# the ID of the status
id_tweet = os.getenv('STATUS_ID')
id_user = os.getenv('USER_ID')
  
# fetching the status
status = api.get_status(id_tweet)

followers = api.get_follower_ids(user_id=id_user)
retweeters = api.get_retweeter_ids(id_tweet)

followers_and_retweeters = intersection(followers, retweeters)

random_number = random.randint(0, len(followers_and_retweeters))

winner = api.get_user(user_id=followers_and_retweeters[random_number])

print(winner.name)

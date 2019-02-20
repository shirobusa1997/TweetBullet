import Configulations.config as config, json
from requests_oauthlib import OAuth1Session

CONSUMER_KEY = config.consumer_key
CONSUMER_SECRET = config.consumer_secret
ACCESS_TOKEN = config.access_token
ACCESS_TOKEN_SECRET = config.access_token_secret
TWITTER_OAUTH = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

RESOURCE_URL = "https://api.twitter.com/1.1/statuses/update.json"

print("Please input details of your posts.")
tweet = input('>> ')

param = {"status" : tweet}

res = TWITTER_OAUTH.post(RESOURCE_URL, params = param)

if res.status_code == 200:
	print("Comfirmed your post.")
else:
	print("Failed : %d"% res.status_code)
# コンフィグデータ参照
import Configulations.config as config, json

# 標準モジュール参照
from requests_oauthlib import OAuth1Session

print("Please input details of your posts.")
tweet = input('>> ')

param = {"status" : tweet}

res = TWITTER_OAUTH.post(RESOURCE_URL, params = param)

if res.status_code == 200:
	print("Comfirmed your post.")
else:
	print("Failed : %d"% res.status_code)

class TWController(Object):
	TW_USER_name = "[UserName]"
	TW_USER_id	 = "[UserID]"

	CONSUMER_KEY 		= 'Unknown'
	CONSUMER_SECRET 	= 'Unknown'
	ACCESS_TOKEN 		= 'Unknown'
	ACCESS_TOKEN_SECRET = 'Unknown'
	TWITTER_OAUTH 		= 'Unknown'

	RESOURCE_URL = "https://api.twitter.com/1.1/statuses/update.json"

	# OAuthによるユーザ認証
	def authorize_user():
		CONSUMER_KEY 		= config.consumer_key
		CONSUMER_SECRET 	= config.consumer_secret
		ACCESS_TOKEN 		= config.access_token
		ACCESS_TOKEN_SECRET = config.access_token_secret
		# OAuthによる認証処理試行
		try:
			TWITTER_OAUTH = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		# すべての例外をキャッチ
		except Exception as e:
			print(e)
			return False
		else :
			print("Authorization Completed.")
			return True

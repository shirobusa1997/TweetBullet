# コンフィグデータ参照
import config, json

# 標準モジュール参照
import sys
from requests_oauthlib import OAuth1Session

# print("Please input details of your posts.")
# tweet = input('>> ')

# param = {"status" : tweet}

# res = TWITTER_OAUTH.post(RESOURCE_URL, params = param)

# if res.status_code == 200:
# 	print("Comfirmed your post.")
# else:
# 	print("Failed : %d"% res.status_code)

class TWController():
	TW_USER_name = "[UserName]"
	TW_USER_id	 = "[UserID]"
	RESOURCE_URL = "https://api.twitter.com/1.1/statuses/update.json"

	# OAuthによるユーザ認証
	def authorize_user(self):
		self.CONSUMER_KEY 		= config.consumer_key
		self.CONSUMER_SECRET 	= config.consumer_secret
		self.ACCESS_TOKEN 		= config.access_token
		self.ACCESS_TOKEN_SECRET = config.access_token_secret
		# OAuthによる認証処理試行
		try:
			self.TWITTER_OAUTH = OAuth1Session(self.CONSUMER_KEY, self.CONSUMER_SECRET, self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
		# すべての例外をキャッチ
		except Exception as e:
			print(e)
			return False
		else :
			print("Authorization Completed.")
			return True

	# ユーザテキストの文字数チェック
	def check_textsize(self, text):
		pass
	
	#
	def post_tweet(self, tweet):
		parameter = {"status" : tweet}
		response = self.TWITTER_OAUTH.post(self.RESOURCE_URL, params = parameter)
		if response.status_code == 200:
			print("Comfirmed post.")
			return True
		else:
			print("Failed : %d"% response.status_code)
			return False

if __name__ == '__main__':
	tmp = TWController()
	if tmp.authorize_user() == True:
		if tmp.post_tweet("hoge") == True:
			print("ALL GREEN")
		else:
			print("ERROR - TW2")
	else:
		print("ERROR - TW1")
	sys.exit()
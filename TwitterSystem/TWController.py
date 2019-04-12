# コンフィグデータ参照
import config, json

# 標準モジュール参照
import sys
import urllib
import webbrowser

import oauth2

import tweepy

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

	REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
	ACCESS_TOKEN_URL  = "https://api.twitter.com/oauth/access_token"
	AUTHENTICATE_URL  = "https://api.twitter.com/oauth/authenticate"

	def __init__(self):
		self.CONSUMER_KEY 		= config.consumer_key
		self.CONSUMER_SECRET 	= config.consumer_secret
		self.app = oauth2.Consumer(self.CONSUMER_KEY, self.CONSUMER_SECRET)

	# アプリケーション認証URL取得
	def get_auth_url(self):
		self.set_request_token_content()
		request_token = self.request_token_content["oauth_token"][0]
		query = urllib.parse.urlencode({"oauth_token": request_token})
		return self.AUTHENTICATE_URL + "?" + query

	# トークン情報を持つ辞書(dict)生成
	def get_access_token_dict(self, PIN):
		oauth_token = self.request_token_content["oauth_token"][0]
		oauth_token_secret = self.request_token_content["oauth_token_secret"][0]
		token = oauth2.Token(oauth_token, oauth_token_secret)
		client = oauth2.Client(self.app, token)
		body = urllib.parse.urlencode({"oauth_verifier": PIN})
		response, content = client.request(self.ACCESS_TOKEN_URL, "POST", body = body)
		return urllib.parse.parse_qs(content.decode())

	# トークン要求のための情報生成
	def set_request_token_content(self):
		client = oauth2.Client(self.app)
		response, content = client.request(self.REQUEST_TOKEN_URL, "GET")
		self.request_token_content = urllib.parse.parse_qs(content.decode())


	# OAuthによるユーザ認証
	def authorize_user(self):
		# self.ACCESS_TOKEN 		= config.access_token
		# self.ACCESS_TOKEN_SECRET = config.access_token_secret
		self.auth_url = self.get_auth_url()
		webbrowser.open(self.auth_url)

		print("PINコードを入力してください。\n", end = "")
		PIN = int(input(">> "))

		self.access_token_content = self.get_access_token_dict(PIN)
		self.ACCESS_TOKEN = self.access_token_content["oauth_token"][0]
		self.ACCESS_TOKEN_SECRET = self.access_token_content["oauth_token_secret"][0]

		print("Authorization Completed.------------------------------------------------")
		print("ACCESS TOKEN        = " + self.ACCESS_TOKEN)
		print("ACCESS TOKEN SECRET = " + self.ACCESS_TOKEN_SECRET)
		print("------------------------------------------------------------------------")

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

	# ツイートのPost
	def post_tweet(self, tweet):
		parameter = {"status" : tweet}
		response = self.TWITTER_OAUTH.post(self.RESOURCE_URL, params = parameter)
		if response.status_code == 200:
			print("Comfirmed post.")
			return True
		else:
			print("Failed : %d"% response.status_code)
			return False

	# ユーザID・名前の取得
	def get_userdata(self):
		pass

# 単体テスト時処理
if __name__ == '__main__':
	tmp = TWController()
	# auth_url = tmp.get_auth_url()
	# webbrowser.open(auth_url)

	# print("PINコードを入力してください。\n", end = "")
	# PIN = int(input(">> "))

	# access_token_content = tmp.get_access_token_dict(PIN)
	# access_token = access_token_content["oauth_token"][0]
	# access_token_secret = access_token_content["oauth_token_secret"][0]

	# print("ACCESS TOKEN        = " + access_token + "\n")
	# print("ACCESS TOKEN SECRET = " + access_token_secret + "\n")

	tmp.authorize_user()

	tmp.post_tweet("Test Tweet from TweetBullets.")

	sys.exit()
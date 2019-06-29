# コンフィグデータ参照
import config, json

# 標準モジュール参照
import sys
import urllib
import webbrowser
import unicodedata

import oauth2

# 外部モジュール参照
import tweepy

from requests_oauthlib import OAuth1Session

# 独自モジュール参照
import MJT_Definitions
from TWAuthController import TWAuthController

class TWController():
	TW_USER_name = "[UserName]"
	TW_USER_id	 = "[UserID]"

	RESOURCE_URL	= "https://api.twitter.com/1.1/statuses/update.json"
	USERLOOKUP_URL	= "https://api.twitter.com/1.1/users/lookup.json"

	REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
	ACCESS_TOKEN_URL  = "https://api.twitter.com/oauth/access_token"
	AUTHENTICATE_URL  = "https://api.twitter.com/oauth/authenticate"

	CACHE_PATH = "__pycache__/"

	# 最大テキスト長(Byte単位で計算)
	text_length = 0
	max_length  = 280

	def __init__(self):
		self.AuthInst = TWAuthController()
		print("TWController : CONSTRUCTOR PROCESS COMPLETE")

	def __del__(self):
		print("TWController : DESTRUCTOR PROCESS COMPLETE")

	# ユーザテキストの文字数計算
	def check_textlength(self, text):
		self.text_length = 0
		for character in text:
			# 全角文字・特殊文字は2文字(Byte)として計算
			if unicodedata.east_asian_width(character) in 'FWA':
				self.text_length += 2
			else:
				self.text_length += 1
		return self.text_length

	# Post可否判定
	def can_post(self):
		if (self.text_length  <= 240 and self.text_length > 0):
			return True
		else:
			return False

	def get_user_image(self):
		try:
			print("get_user_image : " + self.UserObject.profile_image_url_https)
			self.profileimg_path = MJT_Definitions.download_image(self.UserObject.profile_image_url_https, self.CACHE_PATH + "profileimg.")
		except Exception as e:
			print(e)
			sys.exit()
		else:
			print("get_user_image() : NO ERROR")
			return self.profileimg_path

	# ツイートのPost
	def post_tweet(self, tweet):
		try:
			self.AuthInst.APIInst.update_status(status=tweet)
		except Exception as e:
			print(e)
		else:
			print("Comfirmed post.")

# 単体テスト時処理
if (__name__ == '__main__'):
	tmp = TWController()
	# auth_url = tmp.get_auth_url()
	# webbrowser.open(auth_url)

	# print("PINコードを入力してください。\n", end = "")
	# PIN = int(input(">> "))

	# access_token_content = tmp.get_access_token_dict(PIN)
	# access_token = access_token_content["oauth_token"][0]
	# access_token_secret = access_token_content["oauth_token_secret"][0]

	# print("ACCESS TOKEN        = " + access_token + "\n")
	# print("ACCESS TOKEN SECRET = " + access_token_secret + "\n"

	tmp.get_user_image()

	sys.exit()
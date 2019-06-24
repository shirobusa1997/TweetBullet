# コンフィグデータ参照
import config, json

# 標準モジュール参照
import sys
import urllib
import webbrowser
import unicodedata

# OAunth認証用モジュール参照
import oauth2

# 外部モジュール参照
import tweepy
from requests_oauthlib import OAuth1Session

# 独自モジュール
import MJT_Definitions

class TWAuthController():
    TW_User_name = "[UserName]"
    TW_USER_id   = "[UserID"

    RESOURCE_URL	= "https://api.twitter.com/1.1/statuses/update.json"
    USERLOOKUP_URL	= "https://api.twitter.com/1.1/users/lookup.json"

    REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
    ACCESS_TOKEN_URL  = "https://api.twitter.com/oauth/access_token"
    AUTHENTICATE_URL  = "https://api.twitter.com/oauth/authenticate"

    CACHE_PATH = "__pycache__/"

    def __init__(self):
        self.CONSUMER_KEY    = config.consumer_key
        self.CONSUMER_SECRET = config.consumer_secret
        self.app             = oauth2.Consumer(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        print("TWAuthController : CONSTRUCTOR PROCESS COMPLETE")

    def __del__(self):
        print("TWAuthController : DESTRUCTOR PROCESS COMPLETE")

    def get_saved_token(self, fileref):
        list = [string.strip() for string in fileref.readlines()]
        self.ACCESS_TOKEN = list[0]
        self.ACCESS_TOKEN_SECRET = list[1]

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
        self.path = '.savedata'
        try:
            with open(self.path) as fileref:
                self.get_saved_token(fileref)
        except FileNotFoundError:
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

            try:
                with open(self.path, mode="w") as fileref:
                    string = self.ACCESS_TOKEN + "\n" + self.ACCESS_TOKEN_SECRET
                    fileref.write(string)
            except FileNotFoundError as e:
                print("An error occured!")
                print(e)
                sys.exit()
            else:
                print("Saved ")

        # OAuthによる認証処理試行
        try:
            # self.TWITTER_OAUTH = OAuth1Session(self.CONSUMER_KEY, self.CONSUMER_SECRET, self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
            self.OAUTH 		= tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
            self.OAUTH.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
            self.APIInst 	= tweepy.API(self.OAUTH)
            self.UserObject = self.APIInst.me() 
            self.UserName	= self.UserObject.name
            self.UserID		= self.UserObject.screen_name

        # すべての例外をキャッチ
        except Exception as e:
            print(e)
            return False
        else :
            print("Authorization Completed.")
            return True

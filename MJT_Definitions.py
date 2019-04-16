# 標準モジュール参照
import sys
import urllib
import requests

def download_image(resource_url, destpath):
    resource = requests.get(resource_url, stream = True)
    if (resource.status_code == 200):
        try:
            with open(destpath, "wb") as file:
                file.write(resource.content)
        except Exception as e:
            print(e)
            return False
        else:
            return True
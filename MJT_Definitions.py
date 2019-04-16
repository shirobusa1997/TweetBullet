# 標準モジュール参照
import sys
import urllib
import requests
import imghdr

def download_image(resource_url, destpath):
    resource = requests.get(resource_url, stream = True)
    if (resource.status_code == 200):
        try:
            resource_type = imghdr.what(None, resource.content)
            with open(destpath + resource_type, "wb") as file:
                file.write(resource.content)
        except Exception as e:
            print(e)
            print("DEBUG : An error occured!")
            return False
        else:
            print("DEBUG : Download Complete.")
            return True

if (__name__ == "__main__"):
    resource_url = "https://pbs.twimg.com/profile_images/1067860552863469568/2xVnEyfR_normal.jpg"
    destpath     = "__pycache__/result."
    download_image(resource_url, destpath)
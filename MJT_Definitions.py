# 標準モジュール参照
import sys
import urllib
import requests
import imghdr

def download_image(resource_url, destpath):
    resource = requests.get(resource_url, stream = True)
    path = "N/A"
    if (resource.status_code == 200):
        try:
            resource_type = imghdr.what(None, resource.content)
            path = destpath + resource_type
            with open(path, "wb") as file:
                file.write(resource.content)
        except Exception as e:
            return e
        else:
            print("DEBUG : Download Complete.")
            return path

# 単体テスト時処理
if (__name__ == "__main__"):
    resource_url = "https://pbs.twimg.com/profile_images/1067860552863469568/2xVnEyfR_normal.jpg"
    destpath     = "__pycache__/result."
    print(download_image(resource_url, destpath))

    sys.exit()
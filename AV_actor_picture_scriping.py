import requests
import urllib2
from bs4 import *
import time
import numpy as np
import os

suffixes = [
    "a","ka","sa","ta","na","ha","ma",
    "ya","ra","wa"
    ]
suffixes = [
    "a","i","u","e","o",
    "ka","ki","ku","ke","ko",
    "sa","shi","su","se","so",
    "ta","chi","tsu","te","to",
    "na","ni","nu","ne","no",
    "ma","mi","mu","me","mo",
    "ha","hi","fu","he","ho",
    "ya","yu","yo"
    ]
res =  []
for suffix in suffixes:
    tmp += 1
    print(tmp)
    base_url = "http://www.dmm.co.jp/digital/videoa/-/actress/=/keyword="
    url = base_url + suffix + "/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    if soup.find("ul",{"class":"act-box-100"}) is None:
        continue
    recommend_imgs = soup.find("ul",{"class":"act-box-100"}).find_all("img")
    print(recommend_imgs + recommend_names)
    for recommend_img in recommend_imgs:
        imgs = recommend_img.get("src")
        names = recommend_img.get("alt")
        print(names)
        filename = names
        response = requests.get(imgs,allo_redirects = False)
        if response.status_code != 200:
        e = Exception("HTTP status: " + response.status_code)
        raise e
    content_type = response.headers["content-type"]
    if 'image' not in content_type:
        e = Exception("Content-Type: " + content_type)
        raise e

    return response.content
        time.sleep(3)

<div class="list-boxcaptside list-boxpagenation group">
<p>1031人中　1～100人　全11ページ中　1ページ目を表示</p>
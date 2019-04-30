# -*- coding: utf-8 -*-

import urllib.request, urllib.parse
import requests, time
from bs4 import BeautifulSoup

base_url = "https://bookmeter.com"
params_to_search = "&partial=true&sort=recommended&type=japanese&page=1"

keyword = "ビジネスモデル全史 (ディスカヴァー・レボリューションズ)"
keyword = urllib.parse.quote(keyword)

url_to_get_id = base_url + "/search?keyword=" + keyword + params_to_search

# キーワードを含めたurlでリクエストを送る
f = urllib.request.urlopen(url_to_get_id)
html = f.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")


def getParamsToGetReview(offset = 0):
    params = {
        'review_filter': 'none',
        'offset': str(offset),
        'limit': '50'
    }
    return params

def getJsonFromRequest(url, params):
    r = requests.get(url, params=params)
    print(r)
    # ここで例外処理を入れる
    return r.json()

def getReviews(path_to_detail):
    # APIに問い合わせるURL
    url_to_get_review = base_url + path_to_detail + "/reviews.json"
    offset = 0

    while True:
        # 特定の本のレビューをAPIから取得
        params_to_get_review = getParamsToGetReview(offset)
        json_data = getJsonFromRequest(url_to_get_review, params_to_get_review)

        # resourcesの中でfor文を回す→print
        if json_data['resources']:
            for i in json_data['resources']:
                print(i['content_tag'])
            offset += 50
            time.sleep(9)
        else:
            print('取得終了')
            break

# 検索結果に本が存在するか判定
if soup.select('a[href*="/books/"]'):
    getReviews(soup.select('a[href*="/books/"]')[0].get('href'))
else:
    print(soup.select('a[href*="/books/"]'))
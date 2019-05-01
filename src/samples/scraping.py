# -*- coding: utf-8 -*-

import urllib.request, urllib.parse
import requests, time
from bs4 import BeautifulSoup

base_url = "https://bookmeter.com"
params_to_search = "&partial=true&sort=recommended&type=japanese&page=1"

keyword = "ノルウェイの森 上 (講談社文庫)"
keyword = urllib.parse.quote(keyword)

url_to_get_id = base_url + "/search?keyword=" + keyword + params_to_search

# キーワードを含めたurlでリクエストを送る
f = urllib.request.urlopen(url_to_get_id)
html = f.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")


def get_params_to_get_review(offset = 0):
    params = {
        'review_filter': 'none',
        'offset': str(offset),
        'limit': '100'
    }
    return params

def get_json_from_request(url, params):
    r = requests.get(url, params=params)
    print(r)
    # ここで例外処理を入れる
    return r.json()

def get_reviews(path_to_detail):
    # APIに問い合わせるURL
    url_to_get_review = base_url + path_to_detail + "/reviews.json"
    offset = 0

    while True:
        # 特定の本のレビューをAPIから取得
        params_to_get_review = get_params_to_get_review(offset)
        json_data = get_json_from_request(url_to_get_review, params_to_get_review)

        # resourcesの中でfor文を回す→print
        if json_data['resources']:
            with open('src/src/samples/sample_reviews.txt', mode='a', encoding='utf-8') as f:
                for i in json_data['resources']:
                    f.write(i['content_tag'] + "\n")
                print("書き込み完了, offset:", offset)

            offset += 100
            time.sleep(10)
        else:
            print('取得終了')
            break

# 検索結果に本が存在するか判定
if soup.select('a[href*="/books/"]'):
    get_reviews(soup.select('a[href*="/books/"]')[0].get('href'))
else:
    print(soup.select('a[href*="/books/"]'))
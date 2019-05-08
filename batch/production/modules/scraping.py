# -*- coding: utf-8 -*-

import urllib.request, urllib.parse
import requests, time
from bs4 import BeautifulSoup

def get_book_id_from_isbn(isbn):
    base_url = "https://bookmeter.com"
    params_to_search = "&partial=true&sort=recommended&type=japanese&page=1"

    url_to_get_id = base_url + "/search?keyword=" + isbn + params_to_search

    # キーワードを含めたurlでリクエストを送る
    f = urllib.request.urlopen(url_to_get_id)
    html = f.read().decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")

    # 検索結果に本が存在するか判定
    if soup.select('a[href*="/books/"]'):
        book_id = soup.select('a[href*="/books/"]')[0].get('href')
        book_id = int(book_id[book_id.rfind('/')+1:])
        return book_id
    else:
        return None

# -*- coding: utf-8 -*-

import urllib.request, urllib.parse
import time
from bs4 import BeautifulSoup

import modules.books as books

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
        book_id = int(book_id[book_id.rfind('/')+1:])# idのみ抽出
        return book_id
    else:
        return None


# def get_book_name_from_id(book_id):
#     base_url = "https://bookmeter.com/books/"
#     url_to_get_name = base_url + str(book_id)
#     f = urllib.request.urlopen(url_to_get_name)
#     html = f.read().decode("utf-8")
#
#     soup = BeautifulSoup(html, "html.parser")




def get_reviews(book_id):
    print("----------------------------取得開始(" + book_id + ")----------------------------")
    url = "https://bookmeter.com/books/" + str(book_id) + "/reviews.json"
    params = {'review_filter': 'none', 'limit': '100'}
    offset = 0
    file_name = '/src/production/reviews/' + str(book_id) + '.txt'

    # ファイルの作成
    f = open(file_name, 'w')
    f.close()

    while True:
        params['offset'] = str(offset)
        json_data = books.json_from_request(url, params)

        if json_data['resources']:
            with open(file_name, mode='a', encoding='utf-8') as f:
                for i in json_data['resources']:
                    f.write(i['content_tag'] + "\n")
                print("書き込み完了, offset:", offset)

            offset += 100
            time.sleep(10)
        else:
            print('----------------------------取得終了----------------------------')
            break

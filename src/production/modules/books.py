from bs4 import BeautifulSoup
import requests, time

import modules.config as config

def get_books(business_flg):
    url = "https://bookmeter.com/reviews.json"
    session_id = login()
    cookies = dict(_session_id_elk=session_id)
    offset = 0

    while True:
        params = get_params(offset)
        json_data = json_from_request(url, params, cookies)

        book_info = get_book_info_from_json(json_data)
        print("----------------------------レビュー取得成功----------------------------")
        print("offset :", offset)

        book_info = narrow_books(book_info, business_flg)

        if offset > 60:
            break
        else:
            offset += 30 # レビューの投稿頻度が意外と多い為
            time.sleep(5)


def get_params(offset = 0):
    params = {
        'offset': str(offset),
        'limit': '20'
    }
    return params


def get_book_info_from_json(json):
    book_info = []
    for i in json['resources']:
        title = i['contents']['book']['title']
        if title[-1:] == ")":
            title = title[:title.rfind('(')-1] # 出版社名を除く

        book_info.append({
            'book_id' : i['contents']['book']['id'],
            'title' : title,
        })

    return book_info


def narrow_books(book_info, business_flg):
    # 先に楽天apiに問い合わせてスクリーニングする
    narrowed_book_info = narrow_with_genre(book_info, business_flg)
    print("----------------------------ジャンル分け終了----------------------------")
    narrowed_book_info = judge_having_enough_reviews(narrowed_book_info)
    print("----------------------------スクリーニング終了----------------------------")

    return narrowed_book_info


def narrow_with_genre(book_info, business_flg):
    narrowed_book_info = []
    url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
    params = { 'applicationId': config.RAKUTEN_APPLICATION_ID, 'hits': '1' }

    for info in book_info:
        params['title'] = info['title']

        book_genre = get_book_genre(url, params)
        print(info, book_genre)


        if business_flg and book_genre[:6] == "001006": # ビジネス書
            narrowed_book_info.append(info)
            print('ビジネス書')
        elif (not business_flg) and book_genre[:6] == "001004": # 小説
            narrowed_book_info.append(info)
            print('小説')
        else:
            print('該当なし')

        time.sleep(2)

    return narrowed_book_info


def judge_having_enough_reviews(book_info):
    narrowed_book_info = []
    for info in book_info:
        url = "https://bookmeter.com/books/" + str(info['book_id']) + "/reviews.json?review_filter=none&offset=1000&limit=1"
        json_data = json_from_request(url)
        print(info)

        if json_data['resources']: # 1000番目以降にレビューが存在するか
            narrowed_book_info.append(info)
            print("レビュー数1000以上あります！！！！！")
        else:
            print("レビュー数1000以下です。")

        time.sleep(10)

    return narrowed_book_info


def json_from_request(url, params = None, cookies = None):
    fail_count = 0

    while True:
        r = requests.get(url, params=params, cookies=cookies)
        if r.status_code == requests.codes.ok:
            print(r)
            break

        fail_count += 1
        print(r, fail_count*10, "秒待ちます")
        if fail_count == 5:
            print("終了しました")
            exit()

        time.sleep(fail_count*10)

    return r.json()

# 楽天へのリクエストは別メソッドで定義
def get_book_genre(url, params):
    fail_count = 0

    while True:
        r = requests.get(url, params=params)
        print(r)
        if r.status_code in [200, 400, 404]:
            break

        fail_count += 1
        print(fail_count * 10, "秒待ちます")
        if fail_count == 5:
            print("終了しました")
            exit()

        time.sleep(fail_count * 10)

    if 'Items' in r.json(): # errorの場合False
        if r.json()['Items']: # 該当書籍が存在しない場合false
            book_genre = r.json()['Items'][0]['Item']["booksGenreId"]
            return book_genre
    return False


def login():
    payload = {
        'utf8': '✓',
        'session[email_address]': config.EMAIL_ADDRESS,
        'session[password]': config.PASSWORD,
        'session[keep]': '1'
    }

    s = requests.Session()
    r = s.get("https://bookmeter.com/login")

    soup = BeautifulSoup(r.text)
    auth_token = soup.find(attrs={'name': 'authenticity_token'}).get('value')
    # ログインに必要なtokenを追加
    payload['authenticity_token'] = auth_token

    res = s.post('https://bookmeter.com/login', data=payload)
    res.raise_for_status()
    session_id = s.cookies.get('_session_id_elk')
    return session_id

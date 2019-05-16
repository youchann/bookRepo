from bs4 import BeautifulSoup
import requests, time

import modules.config as config
import modules.db as db

def get_books_from_bookmeter():
    url = "https://bookmeter.com/reviews.json"
    session_id = login()
    cookies = dict(_session_id_elk=session_id)
    offset = 33050

    while True:
        params = {'offset': str(offset), 'limit': '20'}
        print("----------------------------レビュー取得開始----------------------------")
        print("offset :", offset)
        # レビューのタイムラインから書籍情報を取得
        json_data = json_from_request(url, params, cookies)
        book_info = get_book_info_from_json(json_data)
        print("----------------------------レビュー取得終了----------------------------")

        book_info = narrow_books(book_info)
        db.insert_book_info(book_info)

        if db.has_enough_data("business"):
            break
        else:
            offset += 50 # レビューの投稿頻度が意外と多い為
            time.sleep(5)


def get_book_from_input():
    print("book_id: ")
    book_id = input()
    print("book_name: ")
    book_name = input()

    book_info = [{'book_id': int(book_id), 'title': str(book_name), 'business_flg': True}]
    book_info = get_isbn(book_info)
    # book_info = narrow_books(book_info)
    db.insert_book_info(book_info)


def get_isbn(book_info):
    url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
    params = {'applicationId': config.RAKUTEN_APPLICATION_ID, 'hits': '1'}
    for info in book_info:
        params['title'] = info['title']
        book_genre_and_isbn = get_book_genre_and_isbn(url, params)
        info['isbn'] = book_genre_and_isbn['isbn']
    return book_info

def get_book_info_from_json(json):
    book_info = []
    for i in json['resources']:
        title = i['contents']['book']['title']
        if title[-1:] == ")":
            title = title[:title.rfind('(')-1] # 出版社名を除く

        book_info.append({
            'book_id' : int(i['contents']['book']['id']),
            'title' : title,
        })

    return book_info


def narrow_books(book_info):
    print("----------------------------ジャンル分け開始----------------------------")
    # ジャンルがビジネスか小説か
    narrowed_book_info = narrow_with_genre(book_info)
    print("----------------------------ジャンル分け終了----------------------------")
    print("----------------------------レビュー数分け開始----------------------------")
    # レビュー数が1000以上あるか
    narrowed_book_info = judge_having_enough_reviews(narrowed_book_info)
    print("----------------------------レビュー数分け終了----------------------------")

    return narrowed_book_info


def narrow_with_genre(book_info):
    narrowed_book_info = []
    url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
    params = { 'applicationId': config.RAKUTEN_APPLICATION_ID, 'hits': '1' }

    for info in book_info:
        params['title'] = info['title']
        book_genre_and_isbn = {}
        book_genre_and_isbn = get_book_genre_and_isbn(url, params)

        if not book_genre_and_isbn:
            print("--------------------------------------------------")
            continue
        else:
            print("title :", info['title'], "genre_id :", book_genre_and_isbn["genre"], "isbn :",
                  book_genre_and_isbn["isbn"])
            info['isbn'] = book_genre_and_isbn['isbn']

        if book_genre_and_isbn["genre"][:6] == "001006": # ビジネス書
            info['business_flg'] = True
            narrowed_book_info.append(info)
            print('→ビジネス書')
        # elif book_genre_and_isbn["genre"][:6] == "001004": # 小説
        #     info['business_flg'] = False
        #     narrowed_book_info.append(info)
        #     print('→小説')
        else:
            print('→該当なし')

        print("--------------------------------------------------")
        time.sleep(2)

    return narrowed_book_info


def judge_having_enough_reviews(book_info):
    narrowed_book_info = []
    for info in book_info:
        url = "https://bookmeter.com/books/" + str(info['book_id']) + "/reviews.json?review_filter=none&offset0&limit=1"
        json_data = json_from_request(url)
        print(info)

        if json_data['metadata']['count'] >= 300:
            narrowed_book_info.append(info)
            print("レビュー数300以上あります！！！！！")
        else:
            print("レビュー数300以下です。")

        print("---------------------------------------------------")
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
def get_book_genre_and_isbn(url, params):
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

    if 'Items' in r.json(): # errorの場合None
        if r.json()['Items']: # 該当書籍が存在しない場合None
            info = {
                'genre': r.json()['Items'][0]['Item']["booksGenreId"],
                'isbn': r.json()['Items'][0]['Item']["isbn"],
            }
            return info
    return None


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

    # クッキーからセッションidを取得
    session_id = s.cookies.get('_session_id_elk')
    return session_id

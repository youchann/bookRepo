from bs4 import BeautifulSoup
import requests, time
from retry import retry
import modules.config as config


def get_books():
    url = 'https://bookmeter.com/reviews.json'
    session_id = login()
    cookies = dict(_session_id_elk=session_id)
    offset = 0

    while True:
        params = get_params(offset)
        json_data = json_from_request(url, params, cookies)

        book_ids = get_book_ids_from_json(json_data)
        print(book_ids)
        book_ids = narrow_ids(book_ids)
        print('抽出id: ', book_ids)

        if offset > 60:
            break
        else:
            offset += 20
            time.sleep(5)


def get_params(offset = 0):
    params = {
        'offset': str(offset),
        'limit': '20'
    }
    return params


def get_book_ids_from_json(json):
    book_ids = []
    for i in json['resources']:
        book_ids.append(i['contents']['book']['id'])

    return book_ids


def narrow_ids(book_ids):
    # 先に楽天apiに問い合わせてスクリーニングする
    narrowed_book_ids = judge_having_enough_reviews(book_ids)

    return narrowed_book_ids


def judge_having_enough_reviews(book_ids):
    narrowed_book_ids = []
    for id in book_ids:
        url = "https://bookmeter.com/books/" + str(id) + "/reviews.json?review_filter=none&offset=1000&limit=1"
        json_data = json_from_request(url)

        if json_data['resources']: # 1000番目以降にレビューが存在するか
            narrowed_book_ids.append(id)
        time.sleep(10)

    return narrowed_book_ids

# 4回の失敗まで許容。失敗ごとに10*失敗回数分待つ
@retry(tries=4, delay=10, backoff=2)
def json_from_request(url, params = None, cookies = None):
    r = requests.get(url, params=params, cookies=cookies)
    print(r)
    return r.json()


def login():
    payload = {
        'utf8': '✓',
        'session[email_address]': config.EMAIL_ADDRESS,
        'session[password]': config.PASSWORD,
        'session[keep]': '1'
    }

    s = requests.Session()
    r = s.get('https://bookmeter.com/login')

    soup = BeautifulSoup(r.text)
    auth_token = soup.find(attrs={'name': 'authenticity_token'}).get('value')
    # ログインに必要なtokenを追加
    payload['authenticity_token'] = auth_token

    res = s.post('https://bookmeter.com/login', data=payload)
    res.raise_for_status()
    session_id = s.cookies.get('_session_id_elk')
    return session_id

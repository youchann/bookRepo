from bs4 import BeautifulSoup
import requests, time
import config


def get_books():
    session_id = login()
    cookies = dict(_session_id_elk=session_id)
    offset = 0
    fail_count = 0

    while True:
        params = get_params(offset)
        r = requests.get('https://bookmeter.com/reviews.json', params=params, cookies=cookies)

        if r.status_code == requests.codes.ok:
            print(r.text)

        else:
            fail_count += 10
            time.sleep(fail_count)
            continue

        if offset > 100:
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


def judge_enough


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

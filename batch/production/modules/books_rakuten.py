import time

import modules.books as books
import modules.scraping as scraping
import modules.config as config
import modules.db as db


def get_books_from_rakuten():# 楽天のランキング経由で取得
    # booksGenreId = 001006 & sort = reviewCount & page = 2 & applicationId = 1006634189914336378
    page = 1
    while True:
        book_info = []
        book_info = get_book_info(page)
        book_info = narrow_books(book_info)

        db.insert_book_info(book_info)

        if db.has_enough_data("business"):
            break
        else:
            page += 1


def get_book_info(page):# jsonデータを整形
    print("----------------------------書籍情報取得開始----------------------------")
    print("page :", page)
    book_info = []
    url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
    params = {'applicationId': config.RAKUTEN_APPLICATION_ID, 'booksGenreId': '001006', 'sort': 'sales'}# ビジネスジャンル
    params['page'] = str(page)

    json_data = books.json_from_request(url, params)
    for i in json_data['Items']:
        book_info.append({
            'title': i['Item']['title'],
            'isbn': i['Item']['isbn']
        })
    print("----------------------------書籍情報取得終了----------------------------")

    return book_info

def narrow_books(book_info):
    narrowed_book_info = []
    print("----------------------------book_id取得開始----------------------------")
    for i in book_info:
        book_id = scraping.get_book_id_from_isbn(i['isbn'])
        print(book_id)
        if book_id:
            i['book_id'] = book_id
            i['business_flg'] = True
            narrowed_book_info.append(i)
        time.sleep(1)
    print("----------------------------book_id取得終了----------------------------")
    print("----------------------------レビュー数ソート開始----------------------------")
    narrowed_book_info = books.judge_having_enough_reviews(narrowed_book_info)
    print("----------------------------レビュー数ソート終了----------------------------")

    return narrowed_book_info


def get_image_url(isbn):# jsonデータを整形
    print("----------------------------画像URL取得開始----------------------------")
    print("isbn :", isbn)
    url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
    params = {'applicationId': config.RAKUTEN_APPLICATION_ID, 'isbn': isbn}

    json_data = books.json_from_request(url, params)
    print("----------------------------画像URL取得終了----------------------------")

    image_url = ""
    if json_data['Items']:
        image_url = json_data['Items'][0]['Item']['largeImageUrl']
    return image_url 

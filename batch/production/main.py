from pprint import pprint
from modules import analyzes, lda, books, books_rakuten

# for i in range(5):
#
#     file_path = '/src/src/production/reviews/sample_reviews' + str(i+1) + '.txt'
#
#     analyzed_reviews = analyzes.analyze_from_file(file_path)
#     # pprint(analyzed_reviews)
#
#
#     lda_model = lda.get_lda_model(analyzed_reviews)
#     pprint(lda_model)


# books.get_books_from_bookmeter()
books_rakuten.get_books_from_rakuten()

# import requests, time
#
# url = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
# params = {
#     'applicationId' : '1006634189914336378',
#     'title' : "ノルウェイの森 上",
#     'hits' : '1',
# }
#
# r = requests.get(url, params=params)
# print(r.json()['Items'][0]['Item']["booksGenreId"])

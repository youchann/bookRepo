from pprint import pprint
from modules import analyzes, lda, books, books_rakuten, db, scraping

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

# bookテーブルを埋めてくれるやつ
# books.get_books_from_bookmeter()
books_rakuten.get_books_from_rakuten()

# レビューを取得してくれるやつ
# book_ids = db.get_book_ids()
# for id in book_ids:
#     print(id)
#     scraping.get_reviews(id)
from pprint import pprint
import time
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

# file_path = '/src/batch/production/reviews/sample_reviews3.txt'
# analyzed_reviews = analyzes.analyze_from_file(file_path)
# # pprint(analyzed_reviews)
# lda_model = lda.get_lda_model(analyzed_reviews)
# for i in lda_model:
#     pprint(i)

# bookテーブルを埋めてくれるやつ
# books.get_books_from_bookmeter()
# books_rakuten.get_books_from_rakuten()
# while True:
#     books.get_book_from_input()

# レビューを取得してくれるやつ
# book_ids = db.get_book_ids()
# for id in book_ids:
#     scraping.get_reviews(str(id[0]))

# db.test_execute()
# exit()

# レビューを分析してくれるやつ(仮)
# file_path = '/src/production/reviews/' + "32" + '.txt'
# analyzed_reviews = analyzes.analyze_from_file(file_path, False) # 名詞
# lda_model = lda.get_lda_model(analyzed_reviews)

# analyzed_reviews_adjective = analyzes.analyze_from_file(file_path, True) # 形容詞
# lda_model_adjective = lda.get_lda_model(analyzed_reviews_adjective)
#
# pprint(lda_model_adjective)
# db.stock_topics(lda_model_adjective, 32, True)


# レビューを分析してくれるやつ
# book_ids = db.get_book_ids()
# for id in book_ids:
#     print(id[0])
#     file_path = '/src/production/reviews/' + str(id[0]) + '.txt'
#     analyzed_reviews = analyzes.analyze_from_file(file_path, False) # 名詞
#     analyzed_reviews_adjective = analyzes.analyze_from_file(file_path, True) # 形容詞
#     lda_model = lda.get_lda_model(analyzed_reviews)
#     lda_model_adjective = lda.get_lda_model(analyzed_reviews_adjective)
#     db.stock_topics(lda_model, int(id[0]), False)
#     db.stock_topics(lda_model_adjective, int(id[0]), True)
#     print(id[0], "が終わりました-------------------------------------------------------------------------")

# 画像URL取得してくれるやつ 
isbns = db.get_isbns()
for isbn in isbns:
    print(isbn[0])
    image_url = books_rakuten.get_image_url(isbn[0])
    if image_url: 
        db.regist_image_url(isbn[0], image_url)
    print(isbn[0], "が終わりました-------------------------------------------------------------------------")
    time.sleep(1)

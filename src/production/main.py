from pprint import pprint
from modules import analyzes, lda, bookmeters

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


bookmeters.get_books()

from pprint import pprint
import analyzes, lda

file_path = '/src/src/production/sample_reviews6.txt'

analyzed_reviews = analyzes.analyze_from_file(file_path)
pprint(analyzed_reviews)


lda_model = lda.get_lda_model(analyzed_reviews)
pprint(lda_model)

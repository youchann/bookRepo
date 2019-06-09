from flask import jsonify, request
from api import app
from api.modules import nlp, models

@app.route('/')
def index():
    keyword = request.args.get('keyword')
    word_list = nlp.analyze_text(keyword)
    similar_word_list = models.get_similar_words(word_list["adjective"])

    return jsonify({
        "analyzed_keywords": word_list,
        "similar_words": similar_word_list,
    })

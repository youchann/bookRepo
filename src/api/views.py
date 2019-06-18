from flask import jsonify, request
from api import app
from api.modules import nlp, models

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    word_list = nlp.analyze_text(keyword)
    similar_word_list = models.get_similar_words(word_list["adjective"])

    return jsonify({
        "analyzed_keywords": word_list,
        "similar_words": similar_word_list,
    })

@app.route('/show_adjective_topics', methods=['POST'])
def show_adjective_topics():
    # 想定しているJSON
    # {
    #     "keyword": "渋谷に12時に集合ね！すごい、はやい",
    #     "noun": ["集合"],
    #     "adjective": ["すごい", "はやい"],
    #     "selected_keywords": ["えぐい", "しゅごい", "魂", "小説"]
    # }
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400

    data_json = nlp.separate_selected_keywords(request.json)

    adjective_topics = models.get_adjective_topics(data_json['noun'], data_json['adjective'])

    return jsonify({
        "adjective_topics": adjective_topics
    })


@app.route('/show_noun_topics', methods=['POST'])
def show_noun_topics():
    # 想定しているJSON
    # {
    #     "book_ids": [1231412412,1241421,12113413,423412413],
    # }
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400

    noun_topics = models.get_noun_topics(request.json['book_ids'])

    return jsonify({
        "noun_topics": noun_topics
    })


@app.route('/get_isbn_from_book_ids', methods=['POST'])
def get_isbn_from_book_ids():
    # 想定しているJSON
    # {
    #     "book_ids": [1231412412,1241421,12113413,423412413],
    # }
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400

    isbn_list = models.get_isbn_from_book_ids(request.json['book_ids'])

    return jsonify({
        "isbn_list": isbn_list
    })


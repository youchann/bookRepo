from flask import jsonify, request
from api import app
from api.modules import nlp, models

@app.route('/')
def index():
    return "hello world"


@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    # models.save_searched_word(keyword)
    word_list = nlp.analyze_text(keyword)
    # FIXME: 形容詞・名詞いずれかのみで類義語を抽出するのはなぜだろう
    similar_word_list = models.get_similar_words(word_list["adjective"]) if word_list["adjective"] else models.get_similar_words(word_list["noun"])

    return jsonify({
        "analyzed_keywords": word_list,
        "similar_words": similar_word_list,
    })


@app.route('/show_adjective_topics', methods=['POST'])
def show_adjective_topics():
    # 想定しているJSON
    # {
    #     "noun": ["集合"],
    #     "adjective": ["すごい", "はやい"],
    #     "selected_keywords": ["えぐい", "しゅごい", "魂", "小説"]
    # }
    # if request.headers['Content-Type'] != 'application/json':
    #     print(request.headers['Content-Type'])
    #     return jsonify(res='error'), 400

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
    # if request.headers['Content-Type'] != 'application/json':
    #     print(request.headers['Content-Type'])
    #     return jsonify(res='error'), 400

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
    # if request.headers['Content-Type'] != 'application/json':
    #     print(request.headers['Content-Type'])
    #     return jsonify(res='error'), 400

    isbn_list = models.get_isbn_from_book_ids(request.json['book_ids'])

    return jsonify({
        "isbn_list": isbn_list
    })


@app.route('/get_info_from_book_ids', methods=['POST'])
def get_info_from_book_ids():
    # 想定しているJSON
    # {
    #     "book_ids": [1231412412,1241421,12113413,423412413],
    # }
    # if request.headers['Content-Type'] != 'application/json':
    #     print(request.headers['Content-Type'])
    #     return jsonify(res='error'), 400

    info_list = models.get_info_from_book_ids(request.json['book_ids'])
    return jsonify({
        "info_list": info_list
    })


@app.route('/get_evaluation_data', methods=['GET'])
def get_evaluation_data():
    evaluation_list = models.get_evaluation_data()
    return jsonify({
        "evaluation_list": evaluation_list,
    })


@app.route('/save_evaluation_data', methods=['POST'])
def save_evaluation_data():
    # 想定しているJSON
    # {
    #     "evaluation_data" : [
    #         {
    #             "evaluation_id": 1,
    #             "evaluation" : 3,
    #         },
    #         {
    #             "evaluation_id": 2,
    #             "evaluation": 4,
    #         },
    #         ...
    #     ]
    # }
    # if request.headers['Content-Type'] != 'application/json':
    #     print(request.headers['Content-Type'])
    #     return jsonify(res='error'), 400

    user_id = models.generate_user_id()
    models.save_evaluation(user_id, request.json['evaluation_data'])

    return "ok"

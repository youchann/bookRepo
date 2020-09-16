import random
from flask import jsonify, request
from api import app
from api.modules import nlp, models

@app.route('/')
def index():
    return jsonify({
        "hello world": "hello world"
    })


@app.route('/register_user', methods=['POST'])
def register_user():
    # 想定しているJSON
    # {
    #     "student_number": 12345678,
    # }

    student_number = request.json["student_number"]
    if type(student_number) is not int:
        return jsonify({
            'message': 'student_numberは数値ではありません'
        }), 500

    user_id = models.register_user(student_number)

    return jsonify({
        "id": user_id 
    })

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    models.save_searched_word(keyword)
    word_list = nlp.analyze_text(keyword)

    if (not word_list["adjective"] and not word_list["noun"]):
        return jsonify({
            'message': '形容詞または名詞が見つかりませんでした'
        }), 500

    similar_word_list = models.get_similar_words(word_list["adjective"] + word_list["noun"])

    return jsonify({
        "analyzed_keywords": word_list,
        "similar_words": similar_word_list,
    })


@app.route('/suggest_keyword')
def suggest_keyword():
    return jsonify({
        "keywords": models.get_suggest_keyword(),
    })


@app.route('/show_noun_topics', methods=['POST'])
def show_noun_topics():
    # 想定しているJSON
    # {
    #     "selected_keywords": ["えぐい", "しゅごい", "魂", "小説"]
    # }
    # if request.headers['Content-Type'] != 'application/json':
    #     print(request.headers['Content-Type'])
    #     return jsonify(res='error'), 400

    noun_topics = models.get_noun_topics(request.json['selected_keywords'])

    return jsonify({
        "noun_topics": random.sample(noun_topics, len(noun_topics))
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

@app.route('/register_book_ids', methods=['POST'])
def register_book_ids():
    # 想定しているJSON
    # {
    #     "user_id": 1,
    #     "book_ids": [1231412412,1241421,12113413,423412413],
    # }
    user_id = request.json["user_id"]
    book_ids = request.json["book_ids"]
    if (not type(user_id) is int or not book_ids):
        return jsonify({
            'message': 'リクエストの形式または型が正しくありません。'
        }), 500

    models.register_book_ids(book_ids, user_id)
    return jsonify(), 204


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

    evaluation_data = request.json['evaluation_data']
    user_id = request.json['user_id']

    if (not type(user_id) is int or not evaluation_data):
        return jsonify({
            'message': 'リクエストの形式または型が正しくありません。'
        }), 500

    models.save_evaluation(user_id, evaluation_data)

    return jsonify(), 204

import sqlalchemy
from pprint import pprint
import os

def get_engine():
    url = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
        'root',                # username
        'root',                # password
        os.environ['DB_HOST'], # server
        'test_database'        # db
    )
    engine = sqlalchemy.create_engine(url, echo=True)

    return engine


def register_user(student_number):
    engine = get_engine()
    sql = "INSERT INTO users(student_number) VALUES (%s)"
    ex = engine.execute(sql, [student_number])
    return ex.lastrowid

def get_similar_words(word_list):
    engine = get_engine()
    word_id = []
    synset_list = []
    similar_words_list = []

    sql = "SELECT `wordid` FROM `word` WHERE `lemma` IN (" + ("%s,"*(len(word_list)))[:-1] + ")"
    ex = engine.execute(sql, word_list)
    for row in ex:
        word_id.append(row[0])

    if not word_id:
        print("類義語は存在しない")
        return []
    else:
        sql = "SELECT `synset` FROM `sense` WHERE `wordid` IN (" + ("%s,"*(len(word_id)))[:-1] + ")"
        ex = engine.execute(sql, word_id)
        for row in ex:
            synset_list.append(row[0])

        sql = "SELECT `lemma` FROM `word`" \
              "WHERE `wordid` IN (SELECT `wordid` FROM `sense` WHERE `synset` IN (" + ("%s,"*(len(synset_list)))[:-1] + "))" \
              "AND `lang` = 'jpn'"
        ex = engine.execute(sql, synset_list)
        for row in ex:
            similar_words_list.append(row[0])

        return similar_words_list


def get_adjective_topics(noun, adjective):
    engine = get_engine()
    topic_ids = []
    book_ids = []

    topic_ids = get_topic_ids_from_words(noun) + get_topic_ids_from_words(adjective)

    if (not topic_ids): return []

    # TODO: ビジネス書or小説の選択に対応させる
    # 形容詞トピックのbook_idを求める
    sql = "SELECT DISTINCT book_id FROM topics " \
            "WHERE id IN (" + ("%s," * (len(topic_ids)))[:-1] + ")"
    ex = engine.execute(sql, topic_ids)

    for row in ex:
        book_ids.append(row[0])

    if (not book_ids): return []

    # 形容詞トピック群を抽出する
    sql = "SELECT topics.id, topics.book_id, words.word FROM topics " \
          "INNER JOIN topic_words ON topics.id = topic_words.topic_id " \
          "INNER JOIN words ON topic_words.word_id = words.id " \
          "WHERE topics.book_id IN (" + ("%s," * (len(book_ids)))[:-1] + ") " \
          "AND topics.adjective_flg = 1"
    ex = engine.execute(sql, book_ids)

    adjective_topics = []
    count = 0
    topic_words = []
    for row in ex:
        topic_words.append(row[2])
        count += 1

        # MEMO: 10単語づつでトピックが切り替わる
        if count == 10:
            adjective_topics.append([row[1], topic_words])
            topic_words = []
            count = 0

    return adjective_topics


def get_noun_topics(book_ids):
    if (not book_ids): return []
    engine = get_engine()

    # 名詞トピック群を抽出する
    sql = "SELECT topics.id,topics.book_id, words.word FROM topics " \
          "INNER JOIN topic_words ON topics.id = topic_words.topic_id " \
          "INNER JOIN words ON topic_words.word_id = words.id " \
          "WHERE topics.book_id IN (" + ("%s," * (len(book_ids)))[:-1] + ") " \
          "AND topics.adjective_flg = 0"
    ex = engine.execute(sql, book_ids)

    noun_topics = []
    count = 0
    topic_words = []
    for row in ex:
        topic_words.append(row[2])
        count += 1

        # MEMO: 10単語づつでトピックが切り替わる
        if count == 10:
            noun_topics.append([row[1], topic_words])
            topic_words = []
            count = 0

    return noun_topics



def get_topic_ids_from_words(words):
    if (not words): return []
    topic_ids = []
    engine = get_engine()
    sql = "SELECT DISTINCT `topic_id` FROM `topic_words` WHERE `word_id` IN" \
          "(SELECT `id` FROM `words` WHERE `word` IN (" + ("%s," * (len(words)))[:-1] + "))"
    ex = engine.execute(sql, words)

    for row in ex:
        topic_ids.append(row[0])

    return topic_ids


def get_isbn_from_book_ids(book_ids):
    if (not book_ids): return []
    isbn_list = []
    engine = get_engine()
    sql = "SELECT `isbn` FROM `books` WHERE `id` IN (" + ("%s," * (len(book_ids)))[:-1] + ")"
    ex = engine.execute(sql, book_ids)

    for row in ex:
        isbn_list.append(row[0])

    return isbn_list


def get_info_from_book_ids(book_ids):
    if (not book_ids): return []
    info_list = []
    engine = get_engine()
    sql = "SELECT `id`, `name`, `image_url` FROM `books` WHERE `id` IN (" + ("%s," * (len(book_ids)))[:-1] + ")"
    ex = engine.execute(sql, book_ids)

    for row in ex:
        info_list.append({
            'id': row[0],
            'name': row[1],
            'image_url': row[2],
        })

    return info_list


def get_evaluation_data():
    engine = get_engine()
    sql = "SELECT `id`, `description` FROM `evaluation_items`"
    ex = engine.execute(sql)

    evaluation_data = []
    for row in ex:
        evaluation_data.append({
            'id': row[0],
            'description': row[1],
        })
    
    return evaluation_data


def save_searched_word(keyword):
    engine = get_engine()
    sql = "INSERT INTO search_words(`word`) VALUES (%s)"
    engine.execute(sql, [keyword])

def register_book_ids(book_ids, user_id):
    if (not book_ids or type(user_id) is not int): return

    engine = get_engine()
    sql = "INSERT INTO selected_books(user_id, book_id) VALUES (%s, %s)"
    for book_id in book_ids:
        engine.execute(sql, [user_id, book_id])

def save_evaluation(user_id, evaluation_data):
    engine = get_engine()
    sql = "INSERT INTO evaluation_data(user_id, evaluation_id, evaluation) VALUES (%s, %s, %s) " \
          "ON DUPLICATE KEY UPDATE user_id=%s, evaluation_id=%s"

    for data in evaluation_data:
        engine.execute(sql, [user_id, data['evaluation_id'], data['evaluation'], user_id, data['evaluation_id']])

import sqlalchemy
import sqlalchemy.orm
from pprint import pprint


def get_engine():
    url = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
        'root',          # username
        'root',          # password
        'db',            # server
        'test_database'  # db
    )
    engine = sqlalchemy.create_engine(url, echo=True)

    return engine


def get_book_ids():
    engine = get_engine()
    # result = engine.execute('SELECT `id` FROM `books`')
    result = engine.execute('SELECT `id` FROM `books` WHERE `id` >= 9816024')

    return result


def insert_book_info(book_info):
    engine = get_engine()
    sql = 'INSERT IGNORE INTO `books` (`id`, `isbn`, `name`, `business_flg`) VALUES (%s, %s, %s, %s)'
    for info in book_info:
        engine.execute(sql, [info['book_id'], info['isbn'], info['title'], info['business_flg']])


def has_enough_data(genre = None):
    engine = get_engine()
    if genre == "novel":
        ex = engine.execute("SELECT COUNT(*) FROM books WHERE business_flg = FALSE")
    elif genre == "business":
        ex = engine.execute("SELECT COUNT(*) FROM books WHERE business_flg = TRUE")
    else:
        ex = engine.execute("SELECT COUNT(*) FROM books")

    for c in ex:
        print(c[0])
        count = c[0]

    if count >= 500:
        print("十分です")
        return True
    else:
        return False


def stock_topics(lda_model, book_id, adjective_flg=False):
    topics_with_id = []

    # 単語をidに変換
    for topic in lda_model:
        topic_words = []
        for word in topic[1]:
            topic_words.append(word[0])
        topics_with_id.append(get_word_ids(topic_words))
    pprint(topics_with_id)

    # topicsテーブルを5個挿入&id取得
    topic_ids = insert_and_get_topic_ids(book_id, adjective_flg)
    pprint(topic_ids)

    # topic_wordsテーブルに挿入
    insert_topic_words(topic_ids, topics_with_id)


def get_word_ids(words):
    # 単語がなければ挿入してid取得、なければid取得
    ids = []
    engine = get_engine()
    sql_to_insert_word = 'INSERT IGNORE INTO `words` (`word`) VALUES (%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s)'
    engine.execute(sql_to_insert_word, [words])

    # insertとid取得の処理は分ける(今回は特別)
    sql_to_get_ids = 'SELECT `id` FROM `words` WHERE `word` IN (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    ex = engine.execute(sql_to_get_ids, [words])
    for id in ex:
        ids.append(id[0])

    del engine
    del ex

    return ids


def insert_and_get_topic_ids(book_id, adjective_flg):
    ids = []
    engine = get_engine()
    sql_to_insert_topics = 'INSERT INTO `topics` (`book_id`, `adjective_flg`) VALUES (%s,%s),(%s,%s),(%s,%s),(%s,%s),(%s,%s)'
    engine.execute(sql_to_insert_topics, [book_id, adjective_flg]*5)

    sql_to_get_ids = 'SELECT `id` FROM `topics` WHERE `book_id` = %s AND `adjective_flg` = %s'
    ex = engine.execute(sql_to_get_ids, [book_id, adjective_flg])
    for id in ex:
        ids.append(id[0])
    
    del engine
    del ex

    return ids


def insert_topic_words(topic_ids, topics_with_id):
    count = 0
    engine = get_engine()
    for topic in topics_with_id:
        sql = 'INSERT INTO `topic_words` (`topic_id`, `word_id`) VALUES ' \
               + '({0},%s),({0},%s),({0},%s),({0},%s),({0},%s),({0},%s),({0},%s),({0},%s),({0},%s),({0},%s)'.format(topic_ids[count])
        engine.execute(sql, topic)
        count += 1
    
    del engine

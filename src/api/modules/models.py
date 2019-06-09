import sqlalchemy
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


def get_similar_words(word_list):
    engine = get_engine()
    word_id = []
    sql = "SELECT `wordid` FROM `word` WHERE `lemma` IN (" + "%s,"*(word_list.len()-1) + "%s)"
    ex = engine.execute(sql, word_list)
    for row in ex:
        word_id.append(row[0])

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
    synset_list = []
    similar_words_list = []

    sql = "SELECT `wordid` FROM `word` WHERE `lemma` IN (" + ("%s,"*(len(word_list)))[:-1] + ") AND `pos` = 'a'"
    ex = engine.execute(sql, word_list)
    for row in ex:
        word_id.append(row[0])

    if not word_id:
        print("類義語は存在しない")
    else:
        sql = "SELECT `synset` FROM `sense` WHERE `wordid` IN (" + ("%s,"*(len(word_id)))[:-1] + ")"
        ex = engine.execute(sql, word_id)
        for row in ex:
            synset_list.append(row[0])

        sql = "SELECT `lemma` FROM `word`" \
              "WHERE `wordid` IN (SELECT `wordid` FROM `sense` WHERE `synset` IN (" + ("%s,"*(len(synset_list)))[:-1] + "))" \
              "AND `lang` = 'jpn' AND `pos` = 'a'"
        ex = engine.execute(sql, synset_list)
        for row in ex:
            similar_words_list.append(row[0])

        return similar_words_list
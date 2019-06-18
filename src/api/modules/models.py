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


def get_adjective_topics(noun, adjective):
    engine = get_engine()
    topic_ids_from_noun = []
    topic_ids_from_adjective = []
    book_ids = []

    if noun: topic_ids_from_noun = get_topic_ids_from_words(noun)
    topic_ids_from_adjective = get_topic_ids_from_words(adjective)

    # 形容詞トピックのbook_idを求める
    if topic_ids_from_noun:
        sql = "SELECT DISTINCT `T1`.`book_id` FROM `topics` `T1`, `topics` `T2` " \
              "WHERE `T1`.`id` IN (" + ("%s," * (len(topic_ids_from_adjective)))[:-1] + ") " \
              "AND `T2`.`id` IN (" + ("%s," * (len(topic_ids_from_noun)))[:-1] + ") " \
              "AND `T1`.`book_id` = `T2`.`book_id`"
        ex = engine.execute(sql, topic_ids_from_adjective+topic_ids_from_noun)
    else:
        sql = "SELECT DISTINCT `book_id` FROM `topics` " \
              "WHERE `id` IN (" + ("%s," * (len(topic_ids_from_adjective)))[:-1] + ")"
        ex = engine.execute(sql, topic_ids_from_adjective)

    for row in ex:
        book_ids.append(row[0])

    # 形容詞トピック群を抽出する
    sql = "SELECT `topics`.`id`,`topics`.`book_id`, `words`.`word` FROM `topics` " \
          "INNER JOIN `topic_words` ON `topics`.`id` = `topic_words`.`topic_id` " \
          "INNER JOIN `words` ON `topic_words`.`word_id` = `words`.`id` " \
          "WHERE `topics`.`book_id` IN (" + ("%s," * (len(book_ids)))[:-1] + ") " \
          "AND `topics`.`adjective_flg` = 1"
    ex = engine.execute(sql, book_ids)

    adjective_topics = []
    count = 0
    topic_words = []
    for row in ex:
        topic_words.append(row[2])
        count += 1

        if count == 10:
            adjective_topics.append([row[1], topic_words])
            topic_words = []
            count = 0

    return adjective_topics


def get_topic_ids_from_words(words):
    topic_ids = []
    engine = get_engine()
    sql = "SELECT DISTINCT `topic_id` FROM `topic_words` WHERE `word_id` IN" \
          "(SELECT `id` FROM `words` WHERE `word` IN (" + ("%s," * (len(words)))[:-1] + "))"
    ex = engine.execute(sql, words)

    for row in ex:
        topic_ids.append(row[0])

    return topic_ids

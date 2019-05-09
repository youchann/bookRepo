import sqlalchemy
import sqlalchemy.orm

# tables = engine.execute('INSERT INTO `words` (`id`, `word`) VALUES (1, "aaaa")')


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
    result = engine.execute('SELECT `id` FROM `books`')

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

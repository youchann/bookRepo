import sqlalchemy

url = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    "docker",       # username
    "docker",       # password
    "127.0.0.1",    # server
    "test_database" # db
)

engine = sqlalchemy.create_engine(url, encodint="utf-8", echo=True)

print(engine)

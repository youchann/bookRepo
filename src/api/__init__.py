from flask import Flask
from flask_cors import CORS

# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
# app.config.from_object('api.config') # 環境変数を設定

# db = SQLAlchemy(app)

import api.views

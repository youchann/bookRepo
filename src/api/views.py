from flask import jsonify
from api import app

@app.route('/')
def index():
    return jsonify({
        "message": "テスト!!"
    })

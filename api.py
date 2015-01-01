import json

from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import *

@app.route('/', methods=['POST'])
def test():
	res = json.loads(request.data)
	return jsonify(**{'id': res['id']})

if __name__=='__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', debug=True, port=port)
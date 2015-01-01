import json

from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from extract_youtube_mp3 import extract_youtube_mp3

import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import *

@app.route('/', methods=['POST'])
def test():
	res = json.loads(request.data)
	linkID = res['id']

	extract_youtube_mp3("https://www.youtube.com/watch?v=" + linkID)

	mFile = None
	
	for file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
		if file.endswith(".mp3"):
			mFile = file

	lFile = LinkFile(videoId = linkID, audioFile = mFile)
	db.session.add(lFile)
	db.session.commit()

	for file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
		if file.endswith(".mp3"):
			os.remove(file)	

	return jsonify(**{'id': linkID})

if __name__=='__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', debug=True, port=port)
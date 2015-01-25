import json, random, io, os

from flask import Flask, jsonify, request, send_file
from flask.ext.sqlalchemy import SQLAlchemy
from extract_youtube_mp3 import extract_youtube_mp3

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
			mFile = open(file).read()

	lFile = LinkFile(videoId = linkID, audioFile = mFile)
	db.session.add(lFile)
	try:
		db.session.commit()
	except:
		db.session.rollback()
		raise
	finally:
		db.session.close()

	for file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
		if file.endswith(".mp3"):
			os.remove(file)	

	return jsonify(**{'id': linkID})


@app.route('/music/<int:get_id>', methods=['GET'])
def getMusic(get_id):
	return send_file(io.BytesIO(LinkFile.query.get(get_id).audioFile), attachment_filename=str(get_id) + ".mp3", as_attachment=True)

@app.route('/music/random', methods=['GET'])
def getRandomMusic():
	allLinkFileIds = LinkFile.query.with_entities(LinkFile.id).all()
	randomInt = random.randint(0, len(allLinkFileIds) - 1)
	musicId = allLinkFileIds[randomInt][0]
	return send_file(io.BytesIO(LinkFile.query.get(musicId).audioFile), attachment_filename="random.mp3", as_attachment=True)

if __name__=='__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', debug=True, port=port)
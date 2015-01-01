from api import db
from sqlalchemy.dialects.postgresql import JSON

class LinkFile(db.Model):
	__tablename__ = 'linkfiles'

	id = db.Column(db.Integer, primary_key=True)
	videoId = db.Column(db.String())
	audioFile = db.Column(db.LargeBinary())

	def __init__(self, videoId, audioFile):
		self.videoId = videoId
		self.audioFile = audioFile

	def __repr__(self):
		return '<LinkFile - id: {}>'.format(self.id)
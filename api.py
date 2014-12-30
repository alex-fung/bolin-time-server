from flask import Flask
from flask.ext.restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id', type=str)

class UploadVideoLink(Resource):
	def post(self):
		args = parser.parse_args()
		id = {'id': args['id']}
		return id, 201
		
api.add_resource(UploadVideoLink, '/')

if __name__=='__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True, port=port)
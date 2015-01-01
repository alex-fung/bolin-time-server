from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import *
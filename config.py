import os

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'Northern-air-temple'
	DATABASE_URL="postgresql://bolin:opalandbolin@bolintimeinstance.c9hc8vdkzflp.us-west-2.rds.amazonaws.com:5432/bolintimedatabase"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
	DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
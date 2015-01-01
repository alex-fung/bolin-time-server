import os

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'Northern-air-temple'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
	DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
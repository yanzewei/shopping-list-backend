import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
from dotenv import find_dotenv,load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Config:
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = "mysql://root:A00429842@localhost/shop"
    #REDIS_URL = "redis://:www123456@localhost:6379/0"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_MYSQL_URL')
    REDIS_URL = os.environ.get('DEV_REDIS_URL')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_MYSQL_URL')
    REDIS_URL = os.environ.get('TEST_REDIS_URL')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_URL')
    REDIS_URL = os.environ.get('REDIS_URL')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

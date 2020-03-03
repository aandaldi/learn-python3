import os


class Config(object):
    DEBUG = True
    SECRET_KEY = 'secret key'


class ProductionConfig(Config):
    ENV = "PRODUCTION"
    DEBUG = False


class DevelopmentConfig(Config):
    ENV = "DEVELOPMENT"
    DEBUG = True
    MONGO_URI = "mongodb://127.0.0.1:27017/mongo1"
    # MONGO_DBNAME = 'buku'


class TestingConfig(Config):
    ENV = "TESTING"
    DEBUG = True
    MONGO_URI = "mongodb://127.0.0.1:27017/mongo2"


config_by_name = dict(
    prod=ProductionConfig,
    dev=DevelopmentConfig,
    test=TestingConfig
)

import os
from os import getenv
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    SECRET_KEY = getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
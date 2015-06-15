import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'thisisnotthesecretyouarelookingfor'
    DEFAULT_DATABASE_URI = "postgresql://localhost/kerbos/"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default=DEFAULT_DATABASE_URI)


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

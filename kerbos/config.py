import os


class DefaultConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'thisisnotthesecretyouarelookingfor'
    DEFAULT_DATABASE_URI = "postgresql://postgres@localhost/kerbos"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default=DEFAULT_DATABASE_URI)


class ProductionConfig(DefaultConfig):
    DEBUG = False


class StagingConfig(DefaultConfig):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(DefaultConfig):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(DefaultConfig):
    TESTING = True


class CircleCIConfig(DefaultConfig):
    TESTING = True
    DEFAULT_DATABASE_URI = "postgresql://ubuntu@localhost/circle_test"


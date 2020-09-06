import os

class Config:
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = 'openapi'
    DEBUG = True
    SECRET_KEY = 'secret'
    API_TITLE = 'timetracker api'
    API_VERSION = '0.1'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('APP_DEVELOPMENT_DATABASE_URI')

    OPENAPI_REDOC_PATH = 'redoc'
    OPENAPI_REDOC_VERSION = 'next'
    OPENAPI_SWAGGER_UI_PATH = 'swagger-ui'
    OPENAPI_SWAGGER_UI_VERSION = '3.18.3'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('APP_TESTING_DATABASE_URI')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('APP_PRODUCTION_DATABASE_URI')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

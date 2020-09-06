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
    # SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'postgres://timetracker:timetracker@rpi4/timetracker'

    OPENAPI_REDOC_PATH = 'redoc'
    OPENAPI_REDOC_VERSION = 'next'
    OPENAPI_SWAGGER_UI_PATH = 'swagger-ui'
    OPENAPI_SWAGGER_UI_VERSION = '3.18.3'


class TestingConfig(Config):
    TESTING = True

    # SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL')


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URL')
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

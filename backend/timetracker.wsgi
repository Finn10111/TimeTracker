import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib/python3.7/site-packages'))
sys.path.insert(1, os.path.dirname(__file__))
activate_this = os.path.join(os.path.dirname(__file__), 'bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
from app import create_app

def application(environ, start_response):
    ENVIRONMENT_VARIABLES = [
        'APP_CONFIG',
        'APP_PRODUCTION_DATABASE_URI',
        'APP_TESTING_DATABASE_URI',
        'APP_DEVELOPMENT_DATABASE_URI'
    ]
    for key in ENVIRONMENT_VARIABLES:
        os.environ[key] = environ.get(key, '')
    app = create_app(os.getenv('APP_CONFIG', 'production'))
    return app(environ, start_response)

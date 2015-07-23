import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import kerbos.shared as Shared


Shared.APP = Flask(__name__)
app = Shared.APP

CONFIG_PATH = 'kerbos.config.' + os.environ.get('APP_SETTINGS', 'DevelopmentConfig')
app.config.from_object(CONFIG_PATH)

Shared.DB = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

def get_app(config):
    config_path = 'kerbos.config.' + os.environ.get('APP_SETTINGS', '%sConfig' % config)
    app.config.from_object(config_path)
    return app

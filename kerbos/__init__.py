import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import kerbos.shared as Shared


# Optionally, set up psycopg2 & SQLAlchemy to be greenlet-friendly.
# Note: psycogreen does not really monkey patch psycopg2 in the
# manner that gevent monkey patches socket.
#
if "PSYCOGREEN" in os.environ:

    # Do our monkey patching
    #
    from gevent.monkey import patch_all
    patch_all()
    from psycogreen.gevent import patch_psycopg
    patch_psycopg()

    using_gevent = True
else:
    using_gevent = False


Shared.APP = Flask(__name__)
app = Shared.APP

CONFIG_PATH = 'kerbos.config.' + os.environ.get('APP_SETTINGS', 'DevelopmentConfig')
app.config.from_object(CONFIG_PATH)

Shared.DB = SQLAlchemy(app)

if using_gevent:

    # Assuming that gevent monkey patched the builtin
    # threading library, we're likely good to use
    # SQLAlchemy's QueuePool, which is the default
    # pool class.  However, we need to make it use
    # threadlocal connections
    #
    #
    Shared.DB.engine.pool._use_threadlocal = True

@app.route('/')
def hello():
    return "Hello hackers :)! Check us out at https://github.com/TranceSquid/kerbos-machine"


def get_app(config):
    config_path = 'kerbos.config.' + os.environ.get('APP_SETTINGS', '%sConfig' % config)
    app.config.from_object(config_path)
    return app

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

import kerbos.main
from kerbos.shared import APP as app, DB as db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run()

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from kerbos import get_app
from kerbos.shared import APP as app, DB as db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app = get_app(config='Development')
    get_app()

@manager.command
def prod():
    app = get_app(config='Production')
    app.run()


if __name__ == '__main__':
    manager.run()

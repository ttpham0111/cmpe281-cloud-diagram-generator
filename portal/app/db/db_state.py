from flask_sqlalchemy import SQLAlchemy


class DatabaseState:
    def __init__(self):
        self.db = None
        self.session = None

    def initialize(self, app, db_url):
        app.config['SQLALCHEMY_DATABASE_URI'] = db_url
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_POOL_SIZE'] = 10
        app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20

        self.db = SQLAlchemy(app)
        self.session = self.db.session


db_state = DatabaseState()

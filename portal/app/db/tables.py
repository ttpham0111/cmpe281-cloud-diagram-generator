from app.db.db_state import db_state

db = db_state.db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    backend_url = db.Column('url', db.String(255), nullable=False)
    mode = db.Column(db.String(10), nullable=False)


class Field(db.Model):
    __tablename__ = 'fields'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(255), db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    value = db.Column(db.String(80), nullable=False)

    user = db.relationship('User', backref='fields')

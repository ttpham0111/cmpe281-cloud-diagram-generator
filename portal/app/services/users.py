import bcrypt

from app.db.tables import User


def get_by_id(user_id, session):
    return session.query(User).filter_by(id=user_id).one()


def get_by_username(username, session):
    return session.query(User).filter_by(username=username).one()


def check_password(user, password):
    return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))

import bcrypt

from app.db.tables import User


def get_by_id(user_id, session):
    return session.query(User).filter_by(user_id=user_id).one()


def check_password(user, password):
    return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))

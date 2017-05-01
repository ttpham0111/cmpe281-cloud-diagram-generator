from collections import namedtuple

import bcrypt


FakeUser = namedtuple('User', 'user_id password')
fake_user = FakeUser('guest', bcrypt.hashpw('guest', bcrypt.gensalt()))


class User:
    @staticmethod
    def get_by_id(user_id):
        return fake_user

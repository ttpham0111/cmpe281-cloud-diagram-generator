from app.api.models.user import User

import bcrypt
from flask import Blueprint, jsonify, request, session

api = Blueprint('api', __name__)


@api.route('/')
def status():
    return jsonify(status='OK'), 200


@api.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        user = User.get_by_id(data['user_id'])
        if bcrypt.checkpw(data['password'].encode('utf-8'), user.password):
            session['user'] = user
            return jsonify({'status': 'OK'}), 200
        else:
            return jsonify({'error': 'Incorrect credentials'}), 400
    except KeyError as e:
        return jsonify({'error': 'The {} field is required'.format(e[0])}), 400
    # except NoResultFound:
    #     return jsonify({'error': 'Incorrect credentials'}), 400


@api.route('/logout')
def logout():
    session.pop('user', None)
    return jsonify({'status': 'OK'}), 200

from flask import Blueprint, jsonify, request, session
from sqlalchemy.orm.exc import NoResultFound

from app.db import users as users_service
from app.db.db_state import db_state


api = Blueprint('api', __name__)


@api.route('/')
def status():
    return jsonify(status='OK'), 200


@api.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        user = users_service.get_by_id(data['user_id'], db_state.session)

        if users_service.check_password(user, data['password']):
            session['user'] = user
            return jsonify({'status': 'OK'}), 200
        else:
            return jsonify({'error': 'Incorrect credentials'}), 400
    except KeyError as e:
        return jsonify({'error': 'The {} field is required'.format(e[0])}), 400
    except NoResultFound:
        return jsonify({'error': 'Incorrect credentials'}), 400


@api.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify(status='OK'), 200


@api.route('/diagram/create', methods=['POST'])
def create_diagram():
    data = request.json
    code = data.get('code')
    file = data.get('file')

    if (not file and not code) or (file and code):
        return jsonify(error='Must provide either a file or code'), 400

    
import base64
from functools import wraps
import os

from flask import Blueprint, jsonify, request, session, url_for
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.utils import secure_filename

from app.services import (users as users_service,
                          grades as grading_service,
                          backend as backend_service)
from app.db.db_state import db_state


api = Blueprint('api', __name__, static_folder='static')


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get('user_id'):
            return jsonify(error='Unauthorized'), 401
        else:
            return f(*args, **kwargs)

    return decorated


@api.route('/')
def status():
    return jsonify(status='OK'), 200


@api.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        user = users_service.get_by_username(data['username'], db_state.session)

        if users_service.check_password(user, data['password']):
            session['user_id'] = user.id

            user_data = {
                'username': user.username,
                'mode': user.mode
            }

            return jsonify(user_data), 200
        else:
            return jsonify({'error': 'Incorrect credentials'}), 400
    except KeyError as e:
        return jsonify({'error': 'The {} field is required'.format(e[0])}), 400
    except NoResultFound:
        return jsonify({'error': 'Incorrect credentials'}), 400


@login_required
@api.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify(status='OK'), 200


@login_required
@api.route('/diagrams/create', methods=['POST'])
def create_diagram():
    user = users_service.get_by_id(session['user_id'], db_state.session)
    try:
        if user.mode == 'file':
            f = request.files['file']
            data = (secure_filename(f.filename), f.read())
        else:
            data = request.json['data']
    except KeyError as e:
        jsonify(error='The {} field is required'.format(e[0]))

    res = backend_service.create_diagram(user.backend_url, data, user.mode)

    filename = res['filename']
    filepath = os.path.join(api.static_folder, 'images', 'diagrams', filename)
    with open(filepath, 'w') as f:
        f.write(base64.b64decode(res['data']))

    return jsonify(url=url_for('api.static', filename='images/diagrams/' + filename)), 201


@login_required
@api.route('/grades', methods=['GET'])
def get_grades():
    db_session = db_state.session
    user = users_service.get_by_id(session['user_id'], db_session)

    fields = grading_service.get_fields(user, db_session)
    return jsonify(fields), 200


@login_required
@api.route('/grades/create', methods=['POST'])
def submit_grading():
    try:
        fields = request.json['fields']
    except KeyError:
        return jsonify(error='A list of grading fields is required'), 400

    db_session = db_state.session
    user = users_service.get_by_id(session['user_id'], db_session)
    for field in fields.itervalues():
        grading_service.create_or_update_field(user, field, db_session)

    return jsonify(status='OK'), 201


@login_required
@api.route('/grades/<field_name>', methods=['DELETE'])
def delete_field(field_name):
    db_session = db_state.session
    user = users_service.get_by_id(session['user_id'], db_session)

    grading_service.delete_field(user, field_name, db_session)

    return jsonify(status='OK'), 200

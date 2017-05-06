import base64
import os
import shutil
import subprocess
from tempfile import NamedTemporaryFile
from uuid import uuid4
from zipfile import ZipFile

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

# Initialize app
app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']


@app.route('/status', methods=['GET'])
def status():
    return jsonify(status='OK'), 200


@app.route('/diagrams/create', methods=['POST'])
def create_diagram():
    mode = os.environ['MODE']
    try:
        if mode == 'file':
            data = get_file_from_request(request)
        else:
            data = request.json['data']
    except KeyError as e:
        return jsonify(error='The {} field is required'.format(e[0])), 400

    output_filename = str(uuid4())
    work_dir = os.path.join(os.environ['TEMP_DIR'], output_filename)
    os.mkdir(work_dir)
    try:
        output_filepath = _create_diagram(data, work_dir, output_filename)
        with open(output_filepath) as f:
            diagram = base64.b64encode(f.read())

    except subprocess.CalledProcessError as e:
        return jsonify(error=e.output), 500

    # finally:
    #     shutil.rmtree(work_dir)

    diagram_filename = os.path.basename(output_filepath)
    return jsonify(data=diagram, filename=diagram_filename), 200


def _create_diagram(data, work_dir, output_filename):
    _data, filename = get_data_from_file(data) if 'filename' in data else (data, '')

    tmp_file = NamedTemporaryFile(dir=work_dir, suffix=os.environ['INPUT_EXT'])
    tmp_file.write(_data)
    tmp_file.seek(0)
    input_path = tmp_file.name

    with open('test', 'w') as f, open(tmp_file.name) as fin:
        f.write(fin.read())
        fin.seek(0)

    ext = os.path.splitext(filename)[1]
    if ext == '.zip':
        unzip(input_path, work_dir)
        input_path = work_dir

    cmd = os.environ['CREATE_DIAGRAM_COMMAND'].format(input_path).split()
    print cmd
    subprocess.check_output(cmd)

    output_filename = output_filename + os.environ['OUTPUT_EXT']
    output_path = os.path.join(work_dir, output_filename)

    if ext == '.zip':
        diagram_path = os.path.join(input_path, 'pic' + os.environ['OUTPUT_EXT'])
    else:
        diagram_path = input_path + os.environ['OUTPUT_EXT']

    os.rename(diagram_path, output_path)
    return output_path


def get_file_from_request(req):
    f = req.files['file']
    return {
        'filename': secure_filename(f.filename),
        'data': f.read()
    }


def get_data_from_file(file_data):
    filename = file_data['filename']
    data = file_data['data']
    return data, filename


def unzip(filepath, dest):
    zipfile = ZipFile(filepath)
    zipfile.extractall(dest)
    zipfile.close()

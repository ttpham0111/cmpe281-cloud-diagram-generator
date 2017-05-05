import requests


def create_diagram(base_url, data, mode):
    url = '{}/{}'.format(base_url, 'diagrams/create')

    if mode == 'file':
        requests_data = {
            'files': {
                'file': data
            }
        }
    else:
        requests_data = {
            'json': {
                'data': data
            }
        }

    res = requests.post(url, **requests_data)
    res.raise_for_status()
    return res.json()

import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
# Здесь должен быть ваш токен
TOKEN = ''
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def create_folder(path):
    create = requests.put(f'{URL}?path={path}', headers=headers)
    return create.status_code


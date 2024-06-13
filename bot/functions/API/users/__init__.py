import requests
from data.config import DOMAIN

def get_all_users():
    url = f'{DOMAIN}/api/users/'
    response = requests.get(url=url)

    return response


def get_user(user_id):
    url = f'{DOMAIN}/api/users/get/'
    response = requests.post(url=url, json={'user_id': user_id})

    return response
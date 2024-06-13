import requests


def update_user_notification(user_id, notification: bool):
    url = 'http://127.0.0.1:8000/api/users/update/notification/'
    data = {'user_id': str(user_id), 'notification': notification}

    response = requests.post(url, json=data)

    return response


def update_user_region(user_id, region: str):
    url = 'http://127.0.0.1:8000/api/users/update/region/'
    data = {'user_id': str(user_id), 'region': region}

    response = requests.post(url, json=data)

    return response
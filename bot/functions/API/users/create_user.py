import requests

def create_user(user_id):
    url = 'http://127.0.0.1:8000/api/users/create/'
    data = {'user_id': str(user_id)}

    response = requests.post(url, json=data)
import requests
from data.config import DOMAIN

def get_user_filter_by_region(region: str):
    url = f'{DOMAIN}/api/users/filter/region/'
    response = requests.post(url, data={'region': region})
    
    try:
        return response.json()['data']
    except:
        return []


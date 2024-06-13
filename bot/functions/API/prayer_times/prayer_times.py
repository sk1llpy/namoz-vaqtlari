import requests
from data.config import DOMAIN

def get_prayer_time(region: str):
    url = f'{DOMAIN}/api/prayer-times/day/'
    response = requests.post(url, data={'region': region})
    return response


def get_prayer_weekly_time(region: str):
    url = f'{DOMAIN}/api/prayer-times/week/'
    response = requests.post(url, data={'region': region})
    return response


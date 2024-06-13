def create_cron_time(prayer_time: str):
    hour, minute = prayer_time.split(":")
    return f'{minute} {hour} * * *'

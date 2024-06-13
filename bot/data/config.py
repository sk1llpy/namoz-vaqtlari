import os
from dotenv import load_dotenv, find_dotenv


dotenv_path = find_dotenv('../.env')
if dotenv_path:
    load_dotenv(dotenv_path)
else:
    raise FileNotFoundError("Error: .env file not found")



BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = os.getenv("ADMINS").split(",") if os.getenv("ADMINS").split(",") else [os.getenv("ADMINS")]
ADMINS = [int(admin) for admin in ADMINS]
DOMAIN = os.getenv("DOMAIN")

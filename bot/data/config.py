import os
from dotenv import load_dotenv, find_dotenv


dotenv_path = find_dotenv('../.env')
if dotenv_path:
    load_dotenv(dotenv_path)
else:
    raise FileNotFoundError("Error: .env file not found")



BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = [int(admin) for admin in os.getenv("ADMINS").split(",")]
DOMAIN = os.getenv("DOMAIN")

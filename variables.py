import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5663282415:AAEFJ28_e09r9rl-5qIVeiE6ijLl-k5R4x4")

API_ID = int(os.environ.get("API_ID", "10300036"))

API_HASH = os.environ.get("API_HASH", "79c295e05c970ddd724f0762ba275104")

PICS = os.environ.get("PICS", "https://telegra.ph/file/34fd203eb89fd747ffb57.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '2124305832').split()]

DB_URL = os.environ.get("DB_URL", "mongodb://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DB_NAME = os.environ.get("DB_NAME", "Cluster0")

RemoveBG_API = os.environ.get("RemoveBG_API", "")

FORCE_SUB = os.environ.get("TheBorzMaf")           

HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")
 
log_channel = environ.get("LOG_CHANNEL")

LOG_CHANNEL = int(log_channel) if log_channel and id_pattern.search(log_channel) else None

LOG_TEXT = """<i><u>👁️‍🗨️USER DETAILS</u>

○ ID : <code>{id}</code>
○ DC : <code>{dc_id}</code>
○ First Name : <code>{first_name}<code>
○ UserName : @{username}

By = {bot}</i>"""













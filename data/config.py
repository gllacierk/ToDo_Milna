import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
DATA_PATH = os.getenv("DATA_PATH")
admin_id = os.getenv("admin_id")

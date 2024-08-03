import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
API_BASE_URL = 'https://global.hoymiles.com/platform/api/gateway'
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
PLANT_ID = os.getenv('PLANT_ID')

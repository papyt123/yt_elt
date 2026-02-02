import requests
import json

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv('API_KEY')
channel_handle = 'MrBeast'  

print(API_KEY)
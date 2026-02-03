import requests
import json

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv('API_KEY')
channel_handle = 'MrBeast'  

print(requests.get(f'https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=1&playlistId=UUX6OQ3DkcsbYNE6H8uQQuVA&key={API_KEY}'))

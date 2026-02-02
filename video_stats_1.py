import requests
import json

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv('API_KEY')
channel_handle = 'MrBeast'  

def get_playlistID():

    try:
        
        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handle}&key={API_KEY}'

        response = requests.get(url)
        print(response)

        data = response.json()            ## json maps pyt types as per json type. {} -> dict , hence comment out 
        print(json.dumps(data,indent=4)) # converts pyt dict into json

        channel_items = data["items"][0]
        channel_playlistID = channel_items["contentDetails"]["relatedPlaylists"]['uploads']
        print(channel_playlistID)
        return channel_playlistID
    
    except requests.exceptions.RequestException as e:
        raise e

if __name__=="__main__":
    get_playlistID()
import requests #we got the play list id using this script
import json
from datetime import date

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv('API_KEY')
channel_handle = 'MrBeast'  

def get_playlistID():

    try:
        
        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handle}&key={API_KEY}'

        response = requests.get(url)
        response.raise_for_status()
        
        print(response)

        data = response.json()            ## json maps pyt types as per json type. {} -> dict 
        #print(json.dumps(data,indent=4)) # it pretty-prints the dictionary d as JSON with an indent of 4 spaces

        channel_items = data["items"][0]
        #print(channel_items)
        channel_playlistID = channel_items["contentDetails"]["relatedPlaylists"]['uploads']
        #print(channel_playlistID)
        return channel_playlistID
        
    except requests.exceptions.RequestException as e:
        raise e

maxResults = 50  
def get_video_ids(playlistID):

    base_url = f'https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId={playlistID}&key={API_KEY}'

    video_ids = [] # list to store all the video ids retrieved, look at the api reference page to see structure 
    pageToken = None # a parameter in the Youtube Data API document

    try:
        while True:
            
            url = base_url

            if pageToken:   # will be False for 1st iter
                url += f"&pageToken={pageToken}" #this is the build of this URL, try changing req params in Youtube Data API document
            response = requests.get(url)
            response.raise_for_status()
            print(response)

            data = response.json() 
            for item in data.get('items', []): #items(type:lst) is a key in the dict-data(has 5 keys) here
                video_id = item['contentDetails']['videoId']
                video_ids.append(video_id)

            pageToken = data.get('nextPageToken') #nextPageToken is a key in dict-data
            if not pageToken:   #pageToken is request parameter
                break
        return video_ids

    except requests.exceptions.RequestException as e:
        raise e
    

def extract_video_data(video_ids): #input parameter is a list
    
    extracted_data = []

    def batch_list(video_id_list, batch_size):
        for video_id in range(0, len(video_id_list), 50):    #here each video_id is a num but not the actual video_id- using range for it
            yield video_id_list[video_id : video_id+ batch_size] # it is a generator object

    try:
        for batch in batch_list(video_ids, maxResults): # will give 50 results per one api call
            video_ids_str = ','.join(batch) # the url can take input as a str too- lets do this for batch of video ids at once

            url = f'https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&part=snippet&part=statistics&id={video_ids_str}&key={API_KEY}'

            response = requests.get(url)
            response.raise_for_status()
            print(response)

            data = response.json()  
            for item in data.get("items", []):
                video_id = item["id"]
                snippet = item["snippet"]
                contentDetails = item["contentDetails"]
                statistics = item["statistics"]

                video_data = {
                    "video_id": video_id,
                    "title": snippet["title"],
                    "publishedAt": snippet["publishedAt"],
                    "duration": contentDetails["duration"],
                    "viewCount": statistics.get("viewCount", None),
                    "likeCount": statistics.get("likeCount", None),
                    "commentCount": statistics.get("commentCount", None),
                }

                extracted_data.append(video_data)

        return extracted_data

    except requests.exceptions.RequestException as e:
        raise e
    
def save_to_json(extracted_data):
    file_path = f"./data/YT_data_{date.today()}.json" # Prepares the file path and name using today's date - nothing created yet

    with open(file_path, "w", encoding="utf-8") as json_outfile: # json_outfile(just a handle to the open file) is a temporary file object used to write data inside this block
        json.dump(extracted_data, json_outfile, indent=4, ensure_ascii=False) # Writes the contents of extracted_data into the file represented by json_outfile in JSON format


if __name__ == '__main__':
    playlistID = get_playlistID()
    video_ids = get_video_ids(playlistID)
    video_data = extract_video_data(video_ids)
    save_to_json(video_data)
    






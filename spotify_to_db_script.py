"""
spotify_to_db_script.py

This script loads the spotify data into the postgres database using the helper files

The script is not efficient as it loads all the needed data at once

Future Planned Versions will use things like pagination to and other things to make data retrieval more efficient and avoid rate limits better
 - I will also convert this from a script into a file containing helper functions maybe housed under a class?

Usage:
    python spotify_to_db_script.py
    
Requirements:
    - Python 3.11
    - dependencies...
    - Spotify API credentials
    - Postgres Database credentials
"""

# Imported Files
import spotify_data_to_db as sds
import spotify_api_connector as sac

import sys
import os
from dotenv import load_dotenv
load_dotenv()

import numpy as np

import json

import time
requests_per_second = 1
    
def main():
    
    # <---------------- Fetch Song Data ---------------->
    
    api_conn_manager = sac.SpotifyApiConnector()
    
    personal_playlists = api_conn_manager.getPersonalPlaylists()
    
    playlists_songs = api_conn_manager.getPlaylistSongs('453J5cNQAqxUmNjWLsr5Wb')
    
    song_features = api_conn_manager.getSongFeatures('','7BqmQ54vDvvZgW689b2SQ2')
    
    # <---------------- Send into Database ---------------->
    
    db_conn_manager = sds.SpotifyDatabaseManager()
    
    
    
    return
        
if __name__ == "__main__":
    main()
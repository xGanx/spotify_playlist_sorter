"""
spotify_data_fetcher.py

This script provides helper functions for fetching data from Spotify

The script is not efficient as it loads all the needed data at once

Future Planned Versions will use things like pagination to and other things to make data retrieval more efficient and avoid rate limits better
 - I will also convert this from a script into a file containing helper functions maybe housed under a class?

Usage:
    Only provides functions
    
Requirements:
    - Python 3.11
    - dependencies...
    - Spotify API credentials
"""
# Imports relating to logging
import sys
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
'''
.debug
.info
.warning
.error
.critical

formatter = logging.Formatter('%()s - ')
handler.setFormatter(formatter)
logging.getLogger().addHAndler(handler)
'''

# https://spotipy.readthedocs.io/en/latest/

# Imports used for loading environment variables
import os
from dotenv import load_dotenv

# Import used for handling JSON repsonse objects
import json

# Typing used for Class Readability
from typing import List

# Imports for the spotipy library
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyApiConnector():
    def __init__(self, scope='user-library-read playlist-modify-public', redirect_uri='http://localhost:3000') -> None:
        self.scope = scope
        self.redirect_uri = redirect_uri
        self._auth_manager = SpotifyOAuth(client_id=os.getenv("CLIENT_ID"),
                                         client_secret=os.getenv("CLIENT_SECRET"),
                                         redirect_uri='http://localhost:3000',
                                         scope='user-library-read playlist-modify-public')
        
        self._sp_client = spotipy.Spotify(auth_manager=self._auth_manager)

    def getPersonalPlaylists(self) -> List:
        # Use to temporarily save playlist json info
        jsonDump = open('Spotify_JSON_Data/personalPlaylistInfo.json','w')
        
        user_playlists = []
        
        cursor=0
        num_playlists = 0
        
        while True:
            try:
                results = self._sp_client.current_user_playlists(limit=50, offset=cursor)
                jsonDump.write(json.dumps(results, indent=4))
            except spotipy.client.SpotifyException as err:
                print(err)
                sys.exit(1)
            num_playlists = results['total']
            
            # print(results)
            
            count = 0
            for _, item in enumerate(results['items']):
                count += 1
                print("%d %s" % (count, item['name']))
                
                user_playlists.append((item['name'],item['id']))
                
            cursor += 50
            if cursor > num_playlists:
                return user_playlists

    # def getPlaylistSongs(playlist_id):
    #     songs = []
        
    #     try:
    #         results = sp_client.playlist_tracks(playlist_id=playlist_id)
    #         jsonDump.write(json.dumps(results, indent=4))
    #     except spotipy.client.SpotifyException as err:
    #             print(err)
    #             sys.exit(1)
        
    #     # print(json.dumps(results, indent=4))
        
    #     # print(results['items'])
        
    #     tracks = results['items']
        
    #     for track in tracks:
    #         # print((track['track']['name'],track['track']['id']))
    #         if track['track']['id'] is None:
    #             continue
    #         songs.append((track['track']['name'],track['track']['id']))
        
    #     return songs

    # def getSongFeatures(song_name, song_id):
    #     global features_to_get
        
    #     print(f'Getting the features for {song_name}...')
        
    #     try:
    #         response = sp_client.audio_features((song_id))
    #         jsonDump.write(json.dumps(response, indent=4))
    #     except spotipy.client.SpotifyException as err:
    #             print(err)
    #             sys.exit(1)
        
    #     features = dict()
    #     for feature in features_to_get:
    #         features[feature] = response[0][feature]
        
    #     # print(response)
        
    #     # print(features)
        
    #     return features

    # def addSongToPlaylist(playlist_id, song_id, playlist_name, song_name):
    #     print(f'Adding {song_name} to the playlist {playlist_name}...')
        
    #     print(f'Playlist id = {playlist_id} | Song id = {song_id}')
        
    #     try:
    #         sp_client.playlist_add_items(playlist_id=playlist_id,items=[song_id])
    #     except spotipy.client.SpotifyException as err:
    #             print(err)
    #             sys.exit(1)
    #     return

    # def addSongListToPlaylist(playlist_id, playlist_name, song_list):
        
    #     for song_name, song_id in song_list:
    #         print(f'Adding {song_name} to the playlist {playlist_name}...')
        
    #         try:
    #             sp_client.playlist_add_items(playlist_id=playlist_id,items=[song_id])
    #         except spotipy.client.SpotifyException as err:
    #             print(err)
    #             sys.exit(1)
    #     return
    
    # Remember about .__dict__
    
    def __str__(self):
        return ''
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
import spotify_data_storage
import spotify_data_fetcher

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
    
    
    
    # <---------------- Send into Database ---------------->
    
    
    
    return
        
if __name__ == "__main__":
    main()
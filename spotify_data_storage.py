"""
spotify_data_storage.py

This script loads the spotify data into the postgres database using the helper files

The script is not efficient as it loads all the needed data at once

Future Planned Versions will use things like pagination to and other things to make data retrieval more efficient and avoid rate limits better
 - I will also convert this from a script into a file containing helper functions maybe housed under a class?

Usage:
    python spotify_data_storage.py
    
Requirements:
    - Python 3.11
    - dependencies...
    - Postgres Database credentials
"""
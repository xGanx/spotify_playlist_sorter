"""
spotify_data_storage.py

This script loads the spotify data into the postgres database using the helper files

The script is not efficient as it loads all the needed data at once

Future Planned Versions will use things like pagination to and other things to make data retrieval more efficient and avoid rate limits better
 - I will also convert this from a script into a file containing helper functions maybe housed under a class?

Usage:
    Only provides functions
    
Requirements:
    - Python 3.11
    - dependencies...
    - Postgres Database credentials
"""
"""
Notes:
 * Is there anything I should specify when creating a database? (connection limit, encoding, template?)
"""


# Imports used for loading environment variables
import os
from dotenv import load_dotenv

# Postgres Database adapater
import psycopg

class SpotifyDatabaseManager:
    def __init__(self, dbname='dev_spotify_data_db', user='postgres', host='localhost', port='5432') -> None:
        self.dbname = dbname
        self.user = user
        self.host = host
        self.port = port
        
        # Connect to postgres server
        with psycopg.connect(
            user=self.user,
            password=os.getenv('DB_PASSWORD'),
            host=self.host,
            port=self.port) as conn:
            
            with conn.cursor() as cur:
                cur.execute(f'SELECT EXISTS ( SELECT datname FROM pg_database WHERE datname=\'{dbname}\');')
        
        db_exists = True
        
        if db_exists:
            self._createDB()
                
        
        
        
    def _createDB(self):
        conn = psycopg.connect(
            user=self.user,
            password=os.getenv('DB_PASSWORD'),
            host=self.host,
            port=self.port
        )
        cursor = conn.cursor()
        try:
            print(f'Creating the database {self.dbname}')
            cursor.execute(f'CREATE DATABASE {self.dbname};')
            print('Database created')
        finally:
            if cursor is not None:
                cursor.close() 
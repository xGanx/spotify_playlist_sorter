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
    
    
Links:
    https://www.psycopg.org/psycopg3/docs/basic/usage.html
"""
"""
Notes:
 * Is there anything I should specify when creating a database? (connection limit, encoding, template?)
 ! need to add logging and exception handling
 ! need to implement async and await for asynchronous functionality
 ! index tables?
"""
# Imports used for loading environment variables
import os
from dotenv import load_dotenv

# Typing used for Class Readability
from typing import List

# Postgres Database adapater
import psycopg

# Import Table Schemas

class SpotifyDatabaseManager:
    def __init__(self, dbname ='dev_spotify_data_db', user='jay', host='localhost', port='5432') -> None:
        self.dbname = 'dev_spotify_data_db'
        self.user = 'jay'
        self.host = 'localhost'
        self.port = '5432'
        
        self._checkDatabaseExistence()
        
        self._createTables()
        
        
            
    def _checkDatabaseExistence(self) -> None:
        result = True
        
        # Connect to postgres server
        with psycopg.connect( # psycopg automatically commits or rolls back at end of block
            user='postgres',
            password=os.getenv('DB_PASSWORD'),
            host=self.host,
            port=self.port) as conn:
            
            # check for database existence
            with conn.cursor() as cur: # psycopg automatically closes cursor at end of block
                cur.execute(f'SELECT EXISTS ( SELECT datname FROM pg_database WHERE datname=\'{self.dbname}\')')
                
                result = cur.fetchone()
            
        if result[0] is False:
            self._createDatabase()
        
    def _createDatabase(self) -> None:
        
        with psycopg.connect(
            user='postgres',
            password=os.getenv('DB_PASSWORD'),
            host=self.host,
            port=self.port,
            autocommit=True) as conn:
            
            with conn.cursor() as cur:
                cur.execute(f'CREATE DATABASE {self.dbname}')
                
    def _createTables(self) -> None:
        
        with psycopg.connect(
            dbname=self.dbname,
            user=self.user,
            password=os.getenv('DB_PASSWORD'),
            host=self.host,
            port=self.port) as conn:
            
            
            
            with conn.cursor() as cur:
                
                
                cur.execute(f"""
                            CREATE TABLE users (
                                id serial PRIMARY KEY,
                                num integer,
                                data text
                            )
                            
                            """)
        
        pass
    
    def insert_data_to_table(self, table, data) -> None:
        
        with psycopg.connect(
            dbname=self.dbname,
            user=self.user,
            password=os.getenv('DB_PASSWORD'),
            host=self.host,
            port=self.port) as conn:
            
            
            
            with conn.cursor() as cur:
                
                
                cur.execute(f"INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
        
        pass
    
    def remove_data_from_table(self, table, data) -> None:
        
        with psycopg.connect(
            dbname=self.dbname,
            user=self.user,
            password=os.getenv('DB_PASSWORD'),
            host=self.host,
            port=self.port) as conn:
            
            
            
            with conn.cursor() as cur:
                
                
                cur.execute(f"""
                            CREATE TABLE users (
                                id serial PRIMARY KEY,
                                num integer,
                                data text
                            )
                            
                            """)
        
        pass
    
    def get_song_data(self, table, data) -> None:
        
        with psycopg.connect(
            dbname=self.dbname,
            user=self.user,
            password=os.getenv('DB_PASSWORD'),
            host=self.host,
            port=self.port) as conn:
            
            
            
            with conn.cursor() as cur:
                
                
                cur.execute(f"""
                            CREATE TABLE users (
                                id serial PRIMARY KEY,
                                num integer,
                                data text
                            )
                            
                            """)
        
        pass
    
    
            
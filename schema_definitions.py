# schema_definitions.py

users_schema = {
    "table_name": "user",
    "columns": [
        {"name": "id", "type": "serial", "primary_key": True},
        {"name": "name", "type": "varchar(255)", "not_null": True},
        {"name": "name", "type": "varchar(255)", "not_null": True},
        # Add more columns as needed
    ]
}

songs_schema = {
    "table_name": "songs",
    "columns": [
        {"name": "id", "type": "serial", "primary_key": True},
        {"name": "value", "type": "integer"},
        # Add more columns as needed
    ]
}

playlist_schema = {
    "table_name": "playlists",
    "columns": [
        {"name": "id", "type": "serial", "primary_key": True},
        {"name": "name", "type": "varchar(255)", "not_null": True},
        # Add more columns as needed
    ]
}

playlist_songs_schema = {
    "table_name": "playlist_songs",
    "columns": [
        {"name": "id", "type": "serial", "primary_key": True},
        {"name": "playlist_id", "type": "varchar(255)", "references": "playlists(playlist_id)"},
        {"name": "song_id", "type": "varchar(255)", "references": "songs(song_id)"},
        # Add more columns as needed
    ]
}
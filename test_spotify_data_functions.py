"""
test_spotify_data_functions.py

This script runs unit tests on functions from spotify_data_fetcher.py 

Usage:
    python spotify_data_fetcher.py
    
Requirements:
    - Python 3.11
    - dependencies...
    - Spotify API credentials
    
    
    https://docs.pytest.org/en/7.1.x/contents.html
"""

import spotify_data_fetcher

#import pytest
import unittest
from unittest.mock import patch

class TestSpotifyDataFunctions(unittest.TestCase):
    
    @patch()
    def test_get_song_data_success(self, mock_request):
        mock_response = ''
        mock_request = mock_response
        
        result = ''
        
        self.assertEqual(result, '')
        
        return
    
    @patch()
    def test_get_song_data_error_handling(self, mock_request):
        mock_response = ''
        mock_request = mock_response
        
        result = ''
        
        self.assertIsNone(result)
        
        return
    


if __name__ == '__main__':
    unittest.main()
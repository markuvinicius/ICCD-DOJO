import os
import unittest
import json
import validators
import requests
from urllib.parse import urlencode
from urllib.request import urlopen

def get_token():
    return "Ht4X4mMzltLWw8oKl5VQMm7tpJbykB8X"

def get_query_string(search, token):
    return urlencode({'q': search.replace('/gif ', ''),'api_key':token, 'limit': 1})

def get_giphy_endpoint(query_string):
    return 'http://api.giphy.com/v1/gifs/search?'+ query_string

def get_gif(api_end_point):
    r = requests.get(api_end_point).json()
    return r['data'][0]['images']['original']['url']


# Classe de teste

class TestPyGiphy(unittest.TestCase):
    
    # testa se a lib está retornando um token
    def test_pygiphy_token(self):
        self.assertIsNotNone(get_token())
    
    # testa se a lib está retornando um token
    def test_pygiphy_get_query_string(self):
        self.assertEquals( get_query_string('dojo','a'), "q=dojo&api_key=a&lang=pt&limit=1" )

    def test_get_giphy_endpoint(self):
        self.assertIsNotNone( validators.url( get_giphy_endpoint(get_query_string('dojo','a') ) ) )

    def test_get_gif(self):
        self.assertIsNotNone( validators.url( get_giphy_endpoint(get_query_string('dojo','a') ) ) )
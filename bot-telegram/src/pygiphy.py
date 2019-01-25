import os
import unittest
import validators
import requests
from urllib.parse import urlencode
from random import choice

def get_token():
    return os.environ['GIPHY_API_TOKEN']


def get_query_string(search, token):
    return urlencode({'q': search.replace('/gif ', ''), 'api_key': token})


def get_giphy_endpoint(query_string):
    return 'http://api.giphy.com/v1/gifs/search?' + query_string


def get_gif(api_end_point):
    r = requests.get(api_end_point).json()    
    if len(r['data']) > 0:              
        image = choice(r['data'])
        return image['images']['original']['url']
    else:
        return None


# Classe de teste
class TestPyGiphy(unittest.TestCase):

    # testa se a lib está retornando um token
    def test_pygiphy_token(self):
        self.assertIsNotNone(get_token())

    # testa se a lib está retornando um token
    def test_pygiphy_get_query_string(self):
        self.assertEqual(get_query_string('dojo', 'a'), "q=dojo&api_key=a&limit=1")

    def test_get_giphy_endpoint(self):
        self.assertIsNotNone(validators.url(get_giphy_endpoint(get_query_string('dojo', 'a'))))

    def test_get_gif(self):
        self.assertIsNotNone(validators.url(get_giphy_endpoint(get_query_string('dojo', 'a'))))

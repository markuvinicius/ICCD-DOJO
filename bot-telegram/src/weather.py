import os
import requests
from urllib.parse import urlencode


def get_token():
    return os.environ['CLIMA_API_TOKEN']


def get_query_string(token):
    return urlencode({'token': token})


def get_endpoint(query):
    return 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/days/15?' + query


def get_by_days(api_end_point):
    r = requests.get(api_end_point).json()
    if len(r['data']) > 0:
        phrase = r['data'][0]['text_icon']['text']['phrase']['reduced']
        day = r['data'][0]['date_br']
        message = 'De forma resumida, ' + 'na data de ' + day + ' terá ' + phrase
        return message
    else:
        return None

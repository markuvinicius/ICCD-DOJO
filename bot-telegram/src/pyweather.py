import os
import requests
from urllib.parse import urlencode

def get_token():
    return os.environ['CLIMA_API_TOKEN']

def get_query_string(token):
    return urlencode({'token': token})

def get_locale(city_name, state):    
    http_params = urlencode({'name':city_name,
                             'state':state,
                             'token':get_token()
                            })

    end_point = 'http://apiadvisor.climatempo.com.br/api/v1/locale/city?'+ http_params        
    r = requests.get(end_point).json()       
    if len(r) > 0:
        return r[0]['id']    
    else:
        return None

def get_current_weather_by_locale_id(locale):
    end_point = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{}/current?token={}'.format(str(locale),get_token())
    r = requests.get(end_point).json()
    result = None

    if r is not None:
        city = r['name']
        state = r['state']
        temperature = r['data']['temperature']
        humidity = r['data']['humidity']
        condition = r['data']['condition']
        sensation = r['data']['sensation']        
        icon = r['data']['icon']

        result = 'No momento, a cidade de {}-{} apresenta {}ºC de temperatura e a atual condição do clima é {}. ' + \
                    'A sensação térmica é de {}ºC e a humidade relativa do ar é {}'

        result = result.format(city,state,temperature,condition,sensation,humidity)
    return result,icon

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

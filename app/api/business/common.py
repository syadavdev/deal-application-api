'''import logging
from datetime import datetime

from app.api.constants import *
from app.api import api_client
from app.api.util import encode_HMACSHA256, decode_hs256_jwt
from flask import current_app as app

log = logging.getLogger(__name__)

def get_api_token():
    cache = Memcache.get_instance()
    token = str((b'None' if cache.get('token') is None else cache.get('token')).decode('UTF-8'))
    if token != 'None':
        return token

    apiKey = app.config['API_KEY']
    apiSecret = app.config['API_SECRET']
    timeFormat = app.config['DATETIME_FORMAT']

    timeStamp = datetime.now().strftime(timeFormat)
    payload = "POST" + timeStamp
    signature = encode_HMACSHA256(payload, apiSecret)

    params = {
        "apiKey": apiKey,
        "signature": signature,
        "timeStamp": timeStamp
    }

    resp = api_client.post(auth_uri, params)

    if resp.get('token', None):
        token = resp.get('token')
    cache.set('token', token)

    return token

def reset_token():
    cache = Memcache.get_instance()
    cache.set('token', None)
    return get_api_token()

def prepare_headers(jwt, custom_headers=None):
    headers = {
        'X-TOKEN': get_api_token(),
    }
    if jwt is None:
        return headers

    user_details = decode_hs256_jwt(jwt, app.config['SECRET_KEY'])
    headers['X-USER'] = user_details.get('name')

    if custom_headers:
        for key,value in custom_headers:
            headers[key] = value

    return headers'''
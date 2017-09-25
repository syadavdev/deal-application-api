import logging, json

from flask_restplus import Api
from app.api.api_exception import ApiException
from .constants import *

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Deal API', description='Deal version 1 APIs')

message = 'An unhandled exception occurred.'

@api.errorhandler
def default_error_handler(e):
    log.exception(message)
    return {error_msg_key: message}, HTTP_STATUS.INTERNAL_SERVER_ERROR

@api.errorhandler(ApiException)
def default_error_handler(e):
    error_code = e.code
    if error_code >= HTTP_STATUS.BAD_REQUEST:
        if isinstance(e.errors, list):
            msg = None
            if len(e.errors) > 0:
                msg = e.errors[0]
                if error_desc_key in msg:
                    msg.pop(error_desc_key)
                msg.pop(error_code_key)
            else:
                msg = {error_msg_key: 'Oops!!! something weird happened'}
            return msg, error_code
        elif isinstance(e.errors, str):
            msg = e.errors
            try:
                msg = json.loads(msg)
                if isinstance(msg, list) and len(msg) > 0:
                    msg = msg[0]
                    if error_desc_key in msg:
                        msg.pop(error_desc_key)
                    msg.pop(error_code_key)
                else:
                    if error_desc_key in msg:
                        msg.pop(error_desc_key)
                    msg.pop(error_code_key)
            except Exception as e:
                msg = {error_msg_key: '{}'.format(msg)}
            return msg, error_code
        else:
            msg = {error_msg_key: '{}'.format(e.errors)}
            return msg, error_code
    return e.errors, HTTP_STATUS.INTERNAL_SERVER_ERROR
r"""const
"""
__version__ = '1.0'

import http.client as HTTP_STATUS

APPLICATION_JSON = 'application/json'

MAX_LIMIT = 2000
MIN_OFFSET = 0

# Keys
username_key = 'userName'
seller_name_key = 'sellerName'
error_msg_key = 'errorMsg'
error_desc_key = 'errorDesc'
error_code_key = 'errorCode'
token_key = 'X-TOKEN'
user_key = 'X-USER'
id_key = 'id'
is_count_key = 'isCount'
limit_key = 'limit'
offset_key = 'offSet'

# End points
auth_uri = '/auth'
login_uri = '/login'
signup_uri= '/signup'
users_uri = '/users'
items_uri = '/itemsList'
user_by_id_uri = '/users/{}'
id_uri = '/<id>'

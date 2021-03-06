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
update_customer_uri = '/updateCustomer'
update_seller_uri = '/updateSeller'
items_add_uri = '/addItem'
items_list_uri = '/getItems'
update_cart_uri = '/addToCart'
get_cart_uri = '/getCart'
create_order_uri = '/createOrder'
get_orders_list_uri = '/getOrdersList'
add_deal_uri = '/addDeal'
get_deal_uri = '/getDeal'
user_by_id_uri = '/users/{}'
id_uri = '/<id>'

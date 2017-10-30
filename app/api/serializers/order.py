from flask_restplus import fields
from app.api.restplus import api

order_credentials = api.model('order_credentials', {
    'paymentMode': fields.String(required=True),
    'cartId': fields.List(fields.Integer,required=True),
    'customerId': fields.Integer(required=True),
})

get_orders = api.model('get_orders', {
    'customerId': fields.Integer(required=True)
})
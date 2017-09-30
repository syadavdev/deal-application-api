from flask_restplus import fields
from app.api.restplus import api

cart_credentials = api.model('cart_credentials', {
    'customerId': fields.Integer(required=True),
    'itemId': fields.Integer(required=True),
    'quantity': fields.Integer(required=True)
})

return_cart = api.model('return_cart', {
    'customerId': fields.Integer(required=True),
})
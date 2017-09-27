from flask_restplus import fields
from app.api.restplus import api

cart_credentials = api.model('cart_credentials', {
    'customerId': fields.Integer(required=True),
    'itemId': fields.Integer(required=True),
    'quantity': fields.Integer(required=True),
    'sellerId' : fields.Integer(required=True)
})
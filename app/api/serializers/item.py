from flask_restplus import fields
from app.api.restplus import api

item_credentials = api.model('item_credentials', {
    'name': fields.String(required=True),
    'price': fields.Float(required=True),
    'sellerId': fields.Integer(required=True)
})
from flask_restplus import fields
from app.api.restplus import api

deals = api.model('deals', {
    'name': fields.String(required=True),
    'price': fields.Float(required=True),
    'sellerId': fields.Integer(required=True)
})
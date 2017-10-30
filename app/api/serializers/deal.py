from flask_restplus import fields
from app.api.restplus import api

add_deals = api.model('add_deals', {
    'itemId': fields.Integer(required=True),
    'description': fields.String(required=True),
    'discount': fields.Float(required=True)
})

get_deals = api.model('get_deals', {
    'itemId': fields.Integer(required=True)
})

from flask_restplus import fields
from app.api.restplus import api

credentials = api.model('signup_credentials', {
    'sellerName': fields.String(required=True),
    'password': fields.String(required=True),
    'email': fields.String(required=True),
    'phoneNumber':fields.String(required=True)
})

login = api.model('login', {
    'phoneNumber':fields.String(readOnly=True),
    'password': fields.String(readOnly=True)
})

new_seller = api.model('new_user', {
    'name': fields.String(required=True),
    'email': fields.String(required=True),
    'phone': fields.String(required=True),
    'roleId': fields.Integer(required=True)
})

update_user = api.model('update_user',{
    'id': fields.Integer,
    'roleId': fields.Integer,
    'phone': fields.String
})

user_resp = api.inherit('user_resp', new_seller, {
    'id': fields.Integer(required=True),
    'countryCode': fields.String(),
    'role': fields.String(required=True),
    'lastLoginTime': fields.String(),
    'isActive': fields.Boolean()
})

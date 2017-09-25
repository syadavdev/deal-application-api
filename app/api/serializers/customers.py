from flask_restplus import fields
from app.api.restplus import api

signup_credentials = api.model('customer_credentials', {
    'userName': fields.String(required=True),
    'password': fields.String(required=True),
    'email': fields.String(required=True),
    'phoneNumber':fields.String(reaquired=True)
})

login = api.model('login', {
    'phoneNumber':fields.String(readOnly=True),
    'password': fields.String(readOnly=True)
})

new_user = api.model('new_user', {
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

user_resp = api.inherit('user_resp', new_user, {
    'id': fields.Integer(required=True),
    'countryCode': fields.String(),
    'role': fields.String(required=True),
    'lastLoginTime': fields.String(),
    'isActive': fields.Boolean()
})

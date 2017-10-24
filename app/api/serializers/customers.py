from flask_restplus import fields
from app.api.restplus import api

signup_credentials = api.model('customer_credentials', {
    'userName': fields.String(required=True),
    'password': fields.String(required=True),
    'email': fields.String(required=True),
    'phoneNumber':fields.String(required=True),
    'shipping':fields.String(),
    'billing':fields.String()
})

login = api.model('login', {
    'phoneNumber':fields.String(readOnly=True),
    'password': fields.String(readOnly=True)
})

update_customer = api.model('update_user',{
    'id':fields.Integer,
    'userName': fields.String(),
    'password': fields.String(),
    'email': fields.String(),
    'phoneNumber':fields.String(),
    'shipping':fields.String(),
    'billing':fields.String()
})

new_user = api.model('new_user', {
    'name': fields.String(required=True),
    'email': fields.String(required=True),
    'phone': fields.String(required=True),
    'roleId': fields.Integer(required=True)
})

user_resp = api.inherit('user_resp', new_user, {
    'id': fields.Integer(required=True),
    'countryCode': fields.String(),
    'role': fields.String(required=True),
    'lastLoginTime': fields.String(),
    'isActive': fields.Boolean()
})

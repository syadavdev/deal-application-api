from flask import request,jsonify
from flask_restplus import Resource

from app.api.business.customer_check import verify_login,get_customer
from app.api.constants import *
from app.api.serializers.customers import *

ns = api.namespace('customers', description='Users related operations')

@ns.route(login_uri)
class Login(Resource):
    """
    login customer
    """
    @api.expect(login)
    def post(self):
        customer_details = request.get_json()
        if(verify_login(customer_details.get('phoneNumber'),customer_details.get('password'))):
            customer_desc = get_customer(customer_details.get('phoneNumber'),customer_details.get('password'))
            return customer_desc,HTTP_STATUS.OK
        else:
            return {'error': 'Unauthorize access'}, HTTP_STATUS.BAD_REQUEST

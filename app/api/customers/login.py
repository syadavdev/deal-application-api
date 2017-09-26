from flask import request
from flask_restplus import Resource

from app.api.business.customer_check import verify_login
from app.api.constants import *
from app.api.serializers.customers import *

ns = api.namespace('customers', description='Users related operations')

@ns.route(login_uri)
class Customers(Resource):
    """
    login customer
    """
    @api.expect(login)
    def post(self):
        customer_details = request.get_json()
        if(verify_login(customer_details.get('phoneNumber'),customer_details.get('password'))):
            return {'success': 'ok'}, HTTP_STATUS.OK
        else:
            return {'Unauthorize access': 'error'}, HTTP_STATUS.BAD_REQUEST

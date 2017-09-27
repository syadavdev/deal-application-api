from flask import request
from flask_restplus import Resource

from app.api.business.customer_check import verify_signup
from app.api.constants import *
from app.api.models.customer import Customer
from app.api.serializers.customers import *

ns = api.namespace('customers', description='Users related operations')


@ns.route(signup_uri)
class Signup(Resource):
    """
    Signup customer
    """
    @api.expect(signup_credentials)
    def post(self):
        customer_details = request.get_json()

        if not verify_signup(customer_details.get('phoneNumber'),customer_details.get('email')):
            customer = Customer(customer_details.get('userName'),
                                customer_details.get('password'),
                                customer_details.get('email'),
                                customer_details.get('phoneNumber'))
            customer.create()
            return {'Signup successfully': 'ok'}, HTTP_STATUS.OK
        else:
            return {'Already Exist Customer', 'error'}, HTTP_STATUS.BAD_REQUEST
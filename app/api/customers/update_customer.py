from flask import request
from flask_restplus import Resource

from app.api.business.customer_check import update_customer_details
from app.api.constants import *
from app.api.models.customer import Customer
from app.api.serializers.customers import *

ns = api.namespace('customers', description='Users related operations')

@ns.route(update_customer_uri)
class UpdateCustomer(Resource):
    """
    Update customer
    """
    @api.expect(update_customer)
    def post(self):
        customer_details = request.get_json()
        id = customer_details.get('id')
        customer = Customer(customer_details.get('userName'),
                            customer_details.get('password'),
                            customer_details.get('email'),
                            customer_details.get('phoneNumber'),
                            customer_details.get('shipping'),
                            customer_details.get('billing'))
        msg,flag = update_customer_details(id,customer)
        if flag:
            return msg, HTTP_STATUS.OK
        else:
            return msg, HTTP_STATUS.BAD_REQUEST
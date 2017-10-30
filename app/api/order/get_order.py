from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.models.order import Order
from app.api.business.order_operation import *
from app.api.serializers.order import *

ns = api.namespace('order', description='order operations')


@ns.route(get_orders_list_uri)
class GetOrder(Resource):
    """
    getting list of Orders
    """

    @api.expect(get_orders)
    def post(self):
        jsonObj = request.get_json()
        customer_id = jsonObj.get('customerId')

        order_desc = get_orders_list(customer_id)
        if order_desc['orders'] != []:
            return order_desc, HTTP_STATUS.OK
        else:
            return {'No orders for you': 'error'}, HTTP_STATUS.NOT_FOUND;
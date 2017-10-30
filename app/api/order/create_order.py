from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.models.order import Order
from app.api.business.order_operation import *
from app.api.serializers.order import *

ns = api.namespace('order', description='order operations')


@ns.route(create_order_uri)
class CreateOrder(Resource):
    """
    Create Order
    """
    @api.expect(order_credentials)
    def post(self):
        order_requirements = request.get_json()
        cart_id_list = order_requirements.get('cartId')
        customer_id = order_requirements.get('customerId')
        payment_mode = order_requirements.get('paymentMode')

        for cart_id in cart_id_list:
            if not check_cart_existance(cart_id, customer_id):
                return {'CustomerId-'+str(customer_id)+' not having this cartId-'+str(cart_id): 'error'}, HTTP_STATUS.BAD_REQUEST

        for cart_id in cart_id_list:
            cart = get_cart(cart_id)
            total_price = get_total_price(cart.item_id,cart.quantity)
            order = Order(payment_mode,
                          cart.item_id,
                          customer_id,
                          cart.quantity,
                          total_price)
            order.create()

        return {'orders Created':'ok'}, HTTP_STATUS.OK


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
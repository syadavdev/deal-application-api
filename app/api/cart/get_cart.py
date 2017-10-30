from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.models.cart import *
from app.api.serializers.cart import *
from app.api.business.cart_check import check_item,get_cart_items,quantity_update

ns = api.namespace('cart', description='cart related operations')


@ns.route(get_cart_uri)
class GetCart(Resource):
    """
    getting cart items
    """
    @api.expect(return_cart)
    def post(self):
        customer_id = request.get_json()
        cart_dics = get_cart_items(customer_id.get('customerId'))

        if(cart_dics['cartItems'] != []):
            return cart_dics, HTTP_STATUS.OK
        else:
            return {'Cart is Empty', 'ok'}, HTTP_STATUS.NOT_FOUND
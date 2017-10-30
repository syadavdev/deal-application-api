from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.models.cart import *
from app.api.serializers.cart import *
from app.api.business.cart_check import check_item,get_cart_items,quantity_update

ns = api.namespace('cart', description='cart related operations')


@ns.route(update_cart_uri)
class AddToCart(Resource):
    """
    Cart
    """
    @api.expect(cart_credentials)
    def post(self):
        cart_details = request.get_json()
        cart = Cart(cart_details.get('customerId'),
                    cart_details.get('itemId'),
                    cart_details.get('quantity'))
        if(check_item(cart.customer_id,cart.item_id)):
            quantity_update(cart.quantity,cart.customer_id,cart.item_id)
        else:
            cart.create()
        return {'Item added to cart': 'ok'}, HTTP_STATUS.OK
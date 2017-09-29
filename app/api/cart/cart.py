from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.models.cart import *
from app.api.serializers.cart import *

ns = api.namespace('cart', description='cart related operations')

@ns.route(cart_uri)
class AddToCart(Resource):
    """
    Cart
    """
    @api.expect(cart_credentials)
    def post(self):
        cart_details = request.get_json()
        cart = Cart(cart_details.get('customerId'),
                    cart_details.get('itemId'),
                    cart_details.get('quantity'),
                    cart_details.get('sellerId'))
        cart.create()
        return {'Item added to cart', 'ok'}, HTTP_STATUS.OK
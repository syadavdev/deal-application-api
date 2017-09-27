from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.serializers.order import *

ns = api.namespace('order', description='order operations')

@ns.route(order_uri)
class Order(Resource):
    """
    Create Order
    """
    @api.expect(order_credentials)
    def post(self):
        return {'success':'ok'}, HTTP_STATUS.OK

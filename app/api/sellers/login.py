from flask import request
from flask_restplus import Resource

from app.api.business.seller_check import verify_login,get_seller
from app.api.constants import *
from app.api.serializers.sellers import *

ns = api.namespace('sellers', description='seller login operations')

@ns.route(login_uri)
class Login(Resource):
    """
    login customer
    """
    @api.expect(login)
    def post(self):
        seller_details = request.get_json()

        if(verify_login(seller_details.get('phoneNumber'),seller_details.get('password'))):
            seller_desc = get_seller(seller_details.get('phoneNumber'),seller_details.get('password'))
            return seller_desc, HTTP_STATUS.OK
        else:
            return {'Unauthorize access':'error'},HTTP_STATUS.BAD_REQUEST

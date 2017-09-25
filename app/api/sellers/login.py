from flask import request
from flask_restplus import Resource
from app.api.serializers.sellers import *
from app.api.constants import *
from app.api.sellers.models.seller import Seller
from app.api.business.seller_check import verify_login

ns = api.namespace('sellers', description='seller login operations')

@ns.route(login_uri)
class Customers(Resource):
    """
    login customer
    """
    @api.expect(login)
    def post(self):
        seller_details = request.get_json()

        if(verify_login(seller_details.get('phoneNumber'),seller_details.get('password'))):
            return {'success':'ok'}, HTTP_STATUS.OK
        else:
            return {'Unauthorize access':'error'},HTTP_STATUS.BAD_REQUEST

import logging

from flask import request
from flask_restplus import Resource

from app.api.business.seller_check import verify_signup
from app.api.constants import *
from app.api.models.seller import Seller
from app.api.serializers.sellers import *

log = logging.getLogger(__name__)

ns = api.namespace('sellers', description='seller login operations')

@ns.route(update_seller_uri)
class UpdateSeller(Resource):
    """
    Update Seller
    """
    @api.expect(update_seller)
    def post(self):
        seller_details = request.get_json()
        seller = Seller(seller_details.get('sellerName'),
                        seller_details.get('password'),
                        seller_details.get('email'),
                        seller_details.get('phoneNumber'),
                        seller_details.get('storeName'),
                        seller_details.get('address'))
        if(not verify_signup(seller.phone_number,seller.email)):
            log.info('Not found so creating one')
            seller.create()
            return {'Signup successfully': 'ok'}, HTTP_STATUS.OK
        else:
            return {'Already Exist Customer','error'}, HTTP_STATUS.BAD_REQUEST

from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.serializers.deal import *
from app.api.business.deal_operation import *

ns = api.namespace('deals', description='deal related operations')


@ns.route(get_deal_uri)
class GetDeal(Resource):
    """
    Getting Deals
    """

    @api.expect(get_deals)
    def post(self):
        json_obj = request.get_json()
        item_id = json_obj.get('itemId')
        if checking_deal(item_id):
            return getting_deal(item_id), HTTP_STATUS.OK
        else:
            return {'No Deal found on this Item', 'error'}, HTTP_STATUS.NOT_FOUND
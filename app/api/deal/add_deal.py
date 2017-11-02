from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.serializers.deal import *
from app.api.models.deal import *
from app.api.business.deal_operation import checking_deal

ns = api.namespace('deals', description='deal related operations')


@ns.route(add_deal_uri)
class AddDeal(Resource):
    """
    Adding Deals
    """
    @api.expect(add_deals)
    def post(self):
        deal_json = request.get_json()
        deal = Deal(deal_json.get('itemId'),
                    deal_json.get('description'),
                    deal_json.get('discount'))

        if not checking_deal(deal.item_id):
            deal.create();
            return {'deal inserted successfully':'ok'},HTTP_STATUS.OK
        else:
            return {'Deal Already Exist On this item': 'error'}, HTTP_STATUS.BAD_REQUEST
from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.serializers.deal import *
from app.api.models.deal import *

ns = api.namespace('deals', description='deal related operations')


@ns.route(add_deal_uri)
class AddDeal(Resource):
    """
    Adding Deals
    """
    @api.expect(add_deals)
    def post(self):
        deal_json = request.get_json()

        return {'success': 'ok'}, HTTP_STATUS.OK
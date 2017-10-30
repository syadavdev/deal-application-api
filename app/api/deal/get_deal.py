from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.serializers.deal import *
from app.api.models.deal import *

ns = api.namespace('deals', description='deal related operations')


@ns.route(get_deal_uri)
class GetDeal(Resource):
    """
    Getting Deals
    """
    @api.expect(get_deals)
    def post(self):
        json_obj = request.get_json();


        return {}, HTTP_STATUS.OK
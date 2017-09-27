from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.serializers.deal import *
from app.api.models.deal import *

ns = api.namespace('deals', description='deal related operations')

@ns.route(deal_uri)
class Item(Resource):
    """
    item details
    """
    @api.expect(deals)
    def post(self):
        item_details = request.get_json()
        item = Item(item_details.get('name'),
                     item_details.get('price'),
                     item_details.get('sellerId'))

        item.create()
        return {'success': 'ok'}, HTTP_STATUS.OK

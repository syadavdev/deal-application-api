from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.serializers.item import *
from app.api.models.item import Item

ns = api.namespace('items', description='Item related operations')

@ns.route(items_uri)
class Items(Resource):
    """
    item details
    """
    @api.expect(item_credentials)
    def post(self):
        item_details = request.get_json()
        item = Item(item_details.get('name'),
                     item_details.get('price'),
                     item_details.get('sellerId'))

        item.create()
        return {'success': 'ok'}, HTTP_STATUS.OK
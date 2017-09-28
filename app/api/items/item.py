import json
from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.serializers.item import *
from app.api.models.item import Item
from app.api.business.item_ops import get_items

ns = api.namespace('items', description='Item related operations')

@ns.route(items_add_uri)
class Item(Resource):
    """
    item details
    """
    @api.expect(item_credentials)
    def post(self):
        item_details = request.get_json()
        item = Item(item_details.get('name'),
                    item_details.get('price'),
                    item_details.get('sellerId'),
                    item_details.get('itemImage'),
                    item_details.get('description'))

        item.create()
        return {'success': 'ok'}, HTTP_STATUS.OK


@ns.route(items_list_uri)
class GetItem(Resource):
    """
    Items list
    """
    @api.expect()
    def get(self):
        items_list = get_items();

        if(items_list['items'] != []):
            return items_list,HTTP_STATUS.OK
        else:
            return {'error': 'No items in table'}, HTTP_STATUS.BAD_REQUEST
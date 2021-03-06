from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.serializers.item import *
from app.api.models.item import Item
from app.api.business.item_operation import get_items,check_item

ns = api.namespace('items', description='Item related operations')


@ns.route(items_add_uri)
class AddItem(Resource):
    """
    item details
    """
    @api.expect(item_credentials)
    def post(self):
        item_details = request.get_json()
        if not check_item(item_details.get('name'),item_details.get('sellerId')):
            item = Item(item_details.get('name'),
                        item_details.get('price'),
                        item_details.get('sellerId'),
                        item_details.get('itemImage'),
                        item_details.get('description'))
            item.create()
            return {'success': 'ok'}, HTTP_STATUS.OK
        else:
            return {'Already in Cart','error'}

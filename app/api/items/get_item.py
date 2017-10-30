from flask import request
from flask_restplus import Resource

from app.api.constants import *
from app.api.serializers.item import *
from app.api.models.item import Item
from app.api.business.item_operation import get_items,check_item

ns = api.namespace('items', description='Item related operations')


@ns.route(items_list_uri)
class GetItem(Resource):
    """
    Items list
    """
    @api.expect()
    def get(self):
        items_list = get_items()

        if items_list['items'] != []:
            return items_list, HTTP_STATUS.OK
        else:
            return {'error': 'Empty Item List'}, HTTP_STATUS.BAD_REQUEST
import logging
from sqlalchemy import *
from app.api.models.item import Item

from app import db

log = logging.getLogger(__name__)

def get_items():
    items_list = db.session.query(Item).order_by(desc(Item.item_id)).all();

    list_of_items = []
    item_disc = {}
    for item in items_list:
        item_disc['itemId'] = item.item_id
        item_disc['name'] = item.item_name
        item_disc['price'] = item.price
        item_disc['sellerId'] = item.seller_id
        item_disc['itemImage'] = item.item_image
        item_disc['desciption'] = item.description
        list_of_items.append(item_disc)

    item_list_desc = {}
    item_list_desc['items'] = list_of_items

    return item_list_desc
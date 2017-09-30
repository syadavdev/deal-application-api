import logging
from sqlalchemy import *
from app.api.models.cart import Cart

from app import db

log = logging.getLogger(__name__)

def get_cart_items(customer_id):
    cart_list = db.session.query(Cart).order_by(desc(Cart.customer_id == customer_id)).all()

    cart_items = []
    cart_item_disc = {}
    for cart in cart_list:
        cart_item_disc['cartId'] = cart.id
        cart_item_disc['customerId'] = cart.customer_id
        cart_item_disc['itemId'] = cart.item_id
        cart_item_disc['quanity'] = cart.quantity
        cart_items.append(cart_item_disc)

    item_list_desc = {}
    item_list_desc['cartItems'] = cart_items
    return item_list_desc

def check_item(customer_id,item_id):
    return db.session.query(exists().where((Cart.customer_id == customer_id)
                                    & (Cart.item_id == item_id))).scalar()

def quantity_update(quantity,customer_id,itemId):
    db_qty = db.session.query(Cart.quantity).filter((Cart.customer_id == customer_id)
                                                     & (Cart.item_id == itemId)).scalar()
    db.session.query(Cart).filter((Cart.customer_id == customer_id)
                            & (Cart.item_id == itemId))\
        .update({"quantity": (db_qty + quantity)})
    db.session.commit()
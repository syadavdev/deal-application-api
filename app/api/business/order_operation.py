import logging
from sqlalchemy import *
from app.api.models.order import Order
from app.api.models.item import Item
from app.api.models.cart import Cart

from app import db


def get_total_price(item_id,quantity):
    item = db.session.query(Item).filter(Item.item_id == item_id).first()
    return item.price * quantity


def check_cart_existance(cart_id, customer_id):
    return db.session.query(Cart).filter((Cart.id == cart_id) & (Cart.customer_id == customer_id)).scalar()


def get_cart(cart_id):
    return db.session.query(Cart).filter(Cart.id == cart_id).first()


def get_orders_list(customer_id):
    order_list = db.session.query(Order).filter(Order.customer_id == customer_id).all()

    list_of_orders = []
    order_disc = {}
    for order in order_list:
        order_disc['orderId'] = order.id
        order_disc['paymentMode'] = order.payment_mode
        order_disc['itemId'] = order.item_id
        order_disc['customerId'] = order.customer_id
        order_disc['quantity'] = order.quantity
        order_disc['totalPrice'] = order.total_price
        list_of_orders.append(order_disc)

    order_list_desc = {'orders': list_of_orders}

    return order_list_desc
import logging

from sqlalchemy import *

from app import db
from app.api.models.seller import Seller

log = logging.getLogger(__name__)


def verify_signup(number,email):
    return db.session.query(exists().where((Seller.phone_number == number)
                                           | (Seller.email == email))).scalar()

def verify_login(number,password):
    return db.session.query(exists().where((Seller.phone_number == number)
                                           & (Seller.password == password))).scalar()

def get_seller(number,password):
    seller =  db.session.query(Seller).filter((Seller.phone_number == number)
                                             & (Seller.password == password)).first()
    seller_desc = {}
    seller_desc['sellerId'] = seller.seller_id
    seller_desc['sellerName'] = seller.seller_name
    seller_desc['phoneNumber'] = seller.phone_number
    seller_desc['email'] = seller.email
    seller_desc['storeName'] = seller.store_name
    seller_desc['address'] = seller.address

    return seller_desc
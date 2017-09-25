from sqlalchemy import *

from app import db
from app.api.sellers.models.seller import Seller
import logging
log = logging.getLogger(__name__)


def verify_signup(number,email):
    return db.session.query(exists().where((Seller.phone_number == number)
                                           | (Seller.email == email))).scalar()

def verify_login(number,password):
    return db.session.query(exists().where((Seller.phone_number == number)
                                           & (Seller.password == password))).scalar()
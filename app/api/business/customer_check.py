from sqlalchemy import *

from app import db
from app.api.customers.models.customer import Customer
import logging
log = logging.getLogger(__name__)


def verify_signup(number,email):
    return db.session.query(exists().where((Customer.phone_number == number)
                                           | (Customer.email == email))).scalar()

def verify_login(number,password):
    return db.session.query(exists().where((Customer.phone_number == number)
                                           & (Customer.password == password))).scalar()
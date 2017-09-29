import logging

from sqlalchemy import *

from app import db
from app.api.models.customer import Customer

log = logging.getLogger(__name__)


def verify_signup(number,email):
    return db.session.query(exists().where((Customer.phone_number == number)
                                           | (Customer.email == email))).scalar()

def verify_login(number,password):
    return db.session.query(exists().where((Customer.phone_number == number)
                                           & (Customer.password == password))).scalar()

def get_customer(number,password):
    customer =  db.session.query(Customer).filter((Customer.phone_number == number)
                                             & (Customer.password == password)).first()
    customer_desc = {}
    customer_desc['id'] = customer.id
    customer_desc['username'] = customer.username
    customer_desc['phoneNumber'] = customer.phone_number
    customer_desc['email'] = customer.email
    customer_desc['shippingAddress'] = customer.shipping_address
    customer_desc['billingAddress'] = customer.billing_address

    return customer_desc
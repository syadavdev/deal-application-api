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


def update_customer_details(customer_id,customer):
    exist = db.session.query(exists().where(Customer.id == customer_id)).scalar()
    if exist:
        duplicate = db.session.query(exists().where((Customer.id != customer_id)
                                                    &(Customer.email == customer.email)
                                                    &(Customer.phone_number == customer.phone_number))) \
            .scalar()
        if not duplicate:
            db.session.query(Customer).filter((Customer.id == customer_id)) \
                .update({'username': customer.username,
                         'phoneNumber' : customer.phone_number,
                         'email': customer.email,
                         'shippingAddress': customer.shipping_address,
                         'billingAddress': customer.billing_address})
            db.session.commit()
            return {'Details update successfully', 'Ok'}, True
        else:
            return {'Info Already exist':'error'},False
    else:
        return{'Wrong Customer_id','error'},False
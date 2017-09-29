# Customer model in db
from app import db


class Customer(db.Model):
    # table
    __tablename__ = 'customer'

    # Columns
    id = db.Column('customerId',db.Integer, primary_key=True, autoincrement=True)
    username = db.Column('username',db.String(100))
    password = db.Column('password',db.String(500))
    email = db.Column('email',db.String(200), unique=True)
    phone_number = db.Column('phoneNumber', db.String(100), unique=True)
    shipping_address = db.Column('shippingAddress',db.String(500))
    billing_address = db.Column('billingAddress',db.String(500))

    def __init__(self, username, password, email, phone_number,shipping_address,billing_address):
        self.username = username
        self.password = password
        self.email = email
        self.phone_number = phone_number
        self.shipping_address = shipping_address
        self.billing_address = billing_address

    def create(self):
        db.session.add(self)
        db.session.commit()
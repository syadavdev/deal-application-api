# User model in db
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

    def __init__(self, username, password, email, phone_number):
        self.username = username
        self.password = password
        self.email = email
        self.phone_number = phone_number

    def create(self):
        db.session.add(self)
        db.session.commit()
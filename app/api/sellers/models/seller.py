from app import db

class Seller(db.Model):
    __tablename__ = 'seller'

    #columns
    seller_id = db.Column('sellerId', db.Integer, primary_key=True, autoincrement=True)
    seller_name = db.Column('sellerName', db.String(100))
    password = db.Column('password', db.String(100))
    email = db.Column('email', db.String(100),unique=True)
    phone_number = db.Column('phoneNumber', db.String(20),unique=True)

    def __init__(self, seller_name, password, email, phone_number):
        self.seller_name = seller_name
        self.password = password
        self.email = email
        self.phone_number = phone_number

    def create(self):
        db.session.add(self)
        db.session.commit()

from app import db

class Seller(db.Model):
    __tablename__ = 'seller'

    #columns
    seller_id = db.Column('sellerId', db.Integer, primary_key=True, autoincrement=True)
    seller_name = db.Column('sellerName', db.String(45),nullable=False)
    password = db.Column('password', db.String(15),nullable=False)
    email = db.Column('email', db.String(45),unique=True,nullable=False)
    phone_number = db.Column('phoneNumber', db.String(13),unique=True,nullable=False)
    store_name = db.Column('storeName',db.String(45),unique=True,nullable=False)
    address = db.Column('address',db.String(45),unique=True,nullable=False)

    def __init__(self, seller_name, password, email, phone_number,store_name,address):
        self.seller_name = seller_name
        self.password = password
        self.email = email
        self.phone_number = phone_number
        self.store_name = store_name
        self.address = address

    def create(self):
        db.session.add(self)
        db.session.commit()

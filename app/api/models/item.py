from app import db


class Item(db.Model):
    #table
    __tablename__ = 'items'

    #columns
    item_id = db.Column('itemId', db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column('name', db.String(100))
    price = db.Column('price', db.Float, nullable=False)
    seller_id = db.Column('sellerId', db.Integer, nullable=False)

    def __init__(self, item_name, price,seller_id):
        self.item_name = item_name
        self.price = price
        self.seller_id = seller_id

    def create(self):
        db.session.add(self)
        db.session.commit()
from app import db


class Item(db.Model):
    #table
    __tablename__ = 'items'

    #columns
    item_id = db.Column('itemId', db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column('name', db.String(100))
    price = db.Column('price', db.Float, nullable=False)
    seller_id = db.Column('sellerId', db.Integer, nullable=False)
    item_image = db.Column('itemImage', db.String(100), nullable=False)
    description = db.Column('description', db.String(500), nullable=False)

    def __init__(self, item_name, price,seller_id,item_image,description):
        self.item_name = item_name
        self.price = price
        self.seller_id = seller_id
        self.item_image = item_image
        self.description = description

    def create(self):
        db.session.add(self)
        db.session.commit()
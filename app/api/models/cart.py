# Cart model in db
from app import db


class Cart(db.Model):
    # table
    __tablename__ = 'cart'

    # Columns
    id = db.Column('cartId',db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column('customerId', db.Integer ,nullable=False);
    item_id = db.Column('itemId',db.Integer, nullable=False)
    quantity = db.Column('quantity',db.Integer, nullable=False)
    seller_id = db.Column('seller_id',db.Integer, nullable=False)

    def __init__(self, customer_id, item_id, quantity,seller_id):
        self.customer_id = customer_id
        self.item_id = item_id
        self.quantity = quantity
        self.seller_id = seller_id

    def create(self):
        db.session.add(self)
        db.session.commit()
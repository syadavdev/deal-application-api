# order model in db
from app import db


class Order(db.Model):
    # table
    __tablename__ = 'order'

    # Columns
    id = db.Column('orderId',db.Integer, primary_key=True, autoincrement=True)
    payment_id = db.Column('paymentMode', db.String ,nullable=False);
    item_id = db.Column('itemId',db.Integer, nullable=False)
    customer_id = db.Column('quantity',db.Integer, nullable=False)
    quantity = db.Column('sellerId',db.Integer, nullable=False)
    total_price = db.Column('totalPrice',db.Float, nullable=False)

    def __init__(self, payment_id, item_id,cusomter_id, quantity, total_price):
        self.payment_id = payment_id
        self.item_id = item_id
        self.customer_id = cusomter_id
        self.quantity = quantity
        self.total_price = total_price

    def create(self):
        db.session.add(self)
        db.session.commit()
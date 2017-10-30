# order model in db
from app import db


class Order(db.Model):
    # table
    __tablename__ = 'order'

    # Columns
    id = db.Column('orderId',db.Integer, primary_key=True, autoincrement=True)
    payment_mode = db.Column('paymentMode', db.String ,nullable=False);
    item_id = db.Column('itemId',db.Integer, nullable=False)
    customer_id = db.Column('customerId',db.Integer, nullable=False)
    quantity = db.Column('quantity',db.Integer, nullable=False)
    total_price = db.Column('totalPrice',db.Float, nullable=False)

    def __init__(self, payment_mode, item_id,cusomter_id, quantity, total_price):
        self.payment_mode = payment_mode
        self.item_id = item_id
        self.customer_id = cusomter_id
        self.quantity = quantity
        self.total_price = total_price

    def create(self):
        db.session.add(self)
        db.session.commit()
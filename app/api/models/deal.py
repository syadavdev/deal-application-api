# deal model in db
from app import db


class Deal(db.Model):
    # table
    __tablename__ = 'deals'

    # Columns
    id = db.Column('id',db.Integer, primary_key=True,nullable=False, autoincrement=True)
    item_id = db.Column('itemId',db.Integer,nullable=False)
    description = db.Column('description',db.String(500),nullable=False)
    discount = db.Column('discount',db.Float,nullable=False)

    def __init__(self, item_id, description, discount):
        self.item_id = item_id
        self.description = description
        self.discount = discount

    def create(self):
        db.session.add(self)
        db.session.commit()
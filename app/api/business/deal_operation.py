import logging
from sqlalchemy import *

from app import db
from app.api.models.deal import Deal

log = logging.getLogger(__name__)


def getting_deal(item_id):
    deal =  db.session.query(Deal).filter((Deal.item_id == item_id)).first()
    return {'id': deal.id,
            'itemId': deal.item_id,
            'description' : deal.description,
            'discount': deal.discount}


def checking_deal(item_id):
    return db.session.query(Deal).filter((Deal.item_id == item_id)).scalar()
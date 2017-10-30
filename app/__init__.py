# Application initialization
import logging.config

from flask import Flask,Blueprint

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from app.api.customers.signup import ns as customer_signup_ns
from app.api.customers.login import ns as customer_login_ns
from app.api.customers.update_customer import ns as customer_updation_ns
from app.api.sellers.signup import ns as seller_signup_ns
from app.api.sellers.login import ns as seller_login_ns
from app.api.items.add_item import ns as add_item_ns
from app.api.items.get_item import ns as get_item_ns
from app.api.cart.add_to_cart import ns as add_cart_ns
from app.api.cart.get_cart import ns as get_cart_ns
from app.api.order.create_order import ns as create_order_ns
from app.api.order.get_order import ns as get_order_ns
from app.api.deal.add_deal import ns as add_deal_ns
from app.api.deal.get_deal import ns as get_deal_ns
from app.api.restplus import api

app = Flask(__name__,static_url_path="",instance_relative_config=False)

logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)

# Load config configuration
app.config.from_object('config.default')
#app.config.from_pyfile('default.py')


def initialize_app(app):
    blueprint = Blueprint('api', __name__, url_prefix='/v1')
    db.init_app(app)
    api.init_app(blueprint)
    api.add_namespace(customer_login_ns)
    api.add_namespace(customer_signup_ns)
    api.add_namespace(customer_updation_ns)

    api.add_namespace(seller_signup_ns)
    api.add_namespace(seller_login_ns)

    api.add_namespace(add_item_ns)
    api.add_namespace(get_item_ns)

    api.add_namespace(add_cart_ns)
    api.add_namespace(get_cart_ns)

    api.add_namespace(get_order_ns)
    api.add_namespace(create_order_ns)
    
    api.add_namespace(add_deal_ns)
    api.add_namespace(get_deal_ns)
    app.register_blueprint(blueprint)


@app.after_request
def allow_origin(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept, X-Token'
    return response

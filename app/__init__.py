# Application initialization
import logging.config

from flask import Flask,Blueprint

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from app.api.customers.signup import ns as customer_signup
from app.api.customers.login import ns as customer_login
from app.api.sellers.signup import ns as seller_signup
from app.api.sellers.login import ns as seller_login
from app.api.items.item import ns as items
from app.api.cart.cart import ns as cart
from app.api.order.order import ns as order
from app.api.deal.deal import ns as deal
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
    api.add_namespace(customer_login)
    api.add_namespace(customer_signup)
    api.add_namespace(seller_signup)
    api.add_namespace(seller_login)
    api.add_namespace(items)
    api.add_namespace(cart)
    api.add_namespace(order)
    app.register_blueprint(blueprint)

@app.after_request
def allow_origin(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept, X-Token'
    return response

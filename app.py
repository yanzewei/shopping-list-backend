from flask import Blueprint
from flask_restful import Api
from services.shoplist import Shoplist
from services.product import Product

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Shoplist, '/shoplist/<int:uid>')
api.add_resource(Product, '/product', endpoint="products")
api.add_resource(Product, '/product/<title>', endpoint="filter_products")
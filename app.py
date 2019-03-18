from flask import Blueprint
from flask_restful import Api
from services.shoplist import Shoplist
from services.product import Product
from services.shopquantity import ShopQuantity

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Shoplist, '/shoplist/<int:uid>', methods=['GET'], endpoint="shoplist_show")
api.add_resource(Shoplist, '/shoplist', methods=['POST', 'PUT', 'DELETE'], endpoint="shoplist_update")
api.add_resource(ShopQuantity, '/shopquantity/<int:uid>')
api.add_resource(Product, '/product', endpoint="products")
api.add_resource(Product, '/product/<title>', endpoint="filter_products")
from flask_restful import Resource
from redismodels import Shoplist as ShopCart

class ShopQuantity(Resource):
    def get(self, uid):
        quantity = ShopCart.get_quantity(uid) 
        return {'status': 'success', 'data': {"quantity":quantity}}, 200

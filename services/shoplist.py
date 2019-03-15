from flask_restful import Resource
from redismodels import Shoplist as ShopCart
from models import *

product_schema = ProductSchema(many=True)
class Shoplist(Resource):
    def get(self, uid):
        carts = ShopCart.get_by_uid(uid) 
        phone_ids = []
        game_machine_ids = []
        for index in carts.keys():
            temp = str(index).split('-')
            if len(temp) == 2:
                if int(temp[0]) == 1:
                    phone_ids.append(temp[1])
                if int(temp[0]) == 2:
                    game_machine_ids.append(temp[1])
        result = []
        if len(phone_ids) > 0:
            phones = db.session.query(Brand, CategoryMobilephone).\
                filter(db.and_(CategoryMobilephone.brand_id==Brand.id,CategoryMobilephone.id.in_(phone_ids))).all()
            phone_attributes = []
            for temp in phones:
                temp[1].logo = temp[0].logo
                temp[1].brand_name = temp[0].name
                temp[1].category = temp[0].category
                phone_attributes.append(temp[1])
            result = product_schema.dump(phone_attributes).data

        if len(game_machine_ids) > 0:
            game_machine = db.session.query(Brand, CategoryGameMachine).\
            filter(db.and_(CategoryGameMachine.brand_id==Brand.id,CategoryGameMachine.id.in_(game_machine_ids))).all()
            game_machine_attributes = [] 
            for temp in game_machine:
                temp[1].logo = temp[0].logo
                temp[1].brand_name = temp[0].name
                temp[1].category = temp[0].category
                game_machine_attributes.append(temp[1])
            result = result + product_schema.dump(game_machine_attributes).data
        return {'status': 'success', 'data': result}, 200

    def post(self):
        return {}

    def put(self):
        return {}

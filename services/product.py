from flask import Flask
from flask_restful import Resource, Api 
from models import *

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def dump_attribtues(self, attributes_arr, query_result):
        for temp in query_result:
            temp[1].logo = temp[0].logo
            temp[1].brand_name = temp[0].name
            temp[1].category = temp[0].category
            attributes_arr.append(temp[1])
        return attributes_arr

    def get(self, title=None):
        product_schema = ProductSchema(many=True)
        limit_num = 20
        if title is None:
            filter_phone_condition = CategoryMobilephone.brand_id==Brand.id
            filter_game_condition = CategoryGameMachine.brand_id==Brand.id
        else:
            filter_phone_condition = db.and_(Brand.name.like(title+"%"), CategoryMobilephone.brand_id==Brand.id)
            filter_game_condition = db.and_(Brand.name.like(title+"%"), CategoryGameMachine.brand_id==Brand.id)
        phones = db.session.query(Brand, CategoryMobilephone).filter(
            filter_phone_condition).order_by(db.text("add_time desc")).limit(limit_num).all()
        phone_attributes = self.dump_attribtues([], phones)
        phones = product_schema.dump(phone_attributes).data
        
        game_machine = db.session.query(Brand, CategoryGameMachine).filter(
            filter_game_condition).order_by(db.text("add_time desc")).limit(limit_num).all()
        game_machine_attributes = self.dump_attribtues([], game_machine)
        game_machine = product_schema.dump(game_machine_attributes).data
        result = {}
        if len(phones) > 0:
            result['phones'] = phones
        if len(game_machine) > 0:
            result['game_machine'] = game_machine
        return {'status': 'success', 'data': result}, 200


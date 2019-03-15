from flask import Flask
from flask_restful import Resource, Api 
from models import *

app = Flask(__name__)
api = Api(app)
product_schema = ProductSchema(many=True)

class Product(Resource):
    def get(self, title=None):
        if title is None:
            filter_condition = CategoryMobilephone.brand_id==Brand.id
        else:
            filter_condition = db.and_(Brand.name==title, CategoryMobilephone.brand_id==Brand.id)
        phones = db.session.query(Brand, CategoryMobilephone).\
            filter(filter_condition).order_by(db.text("add_time desc")).limit(20).all()
        phone_attributes = []
        for temp in phones:
            temp[1].logo = temp[0].logo
            temp[1].brand_name = temp[0].name
            temp[1].category = temp[0].category
            phone_attributes.append(temp[1])
        phones = product_schema.dump(phone_attributes).data
        if title is None:
            filter_condition = CategoryGameMachine.brand_id==Brand.id
        else:
            filter_condition = db.and_(Brand.name==title, CategoryGameMachine.brand_id==Brand.id)
        game_machine = db.session.query(Brand, CategoryGameMachine).\
            filter(filter_condition).order_by(db.text("add_time desc")).limit(20).all()
        game_machine_attributes = [] 
        for temp in game_machine:
            temp[1].logo = temp[0].logo
            temp[1].brand_name = temp[0].name
            temp[1].category = temp[0].category
            game_machine_attributes.append(temp[1])
        game_machine = product_schema.dump(game_machine_attributes).data
        return {'status': 'success', 'data': {'phone':phones, 'game machine':game_machine}}, 200


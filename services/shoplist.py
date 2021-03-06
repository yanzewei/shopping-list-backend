from flask import request
from flask_restful import Resource
from redismodels import Shoplist as ShopCart
from models import *


class Shoplist(Resource):
    def dump_attributes(self, attributes_arr, query_result, id_num_pairs):
        for temp in query_result:
            if temp[1].id in id_num_pairs:
                temp[1].logo = temp[0].logo
                temp[1].brand_name = temp[0].name
                temp[1].category = temp[0].category
                temp[1].num = id_num_pairs[temp[1].id]
                attributes_arr.append(temp[1])
        return attributes_arr

    def get(self, uid):
        product_schema = ProductSchema(many=True)
        carts = ShopCart.get_by_uid(uid) 
        phone_ids = {}
        game_machine_ids = {}
        for index,num in carts.items():
            temp = index.split('-')
            if len(temp) == 2:
                if int(temp[0]) == 1:
                    phone_ids[int(temp[1])] = int(num)
                if int(temp[0]) == 2:
                    game_machine_ids[int(temp[1])] = int(num)
        result = []
        if len(phone_ids) > 0:
            phones = db.session.query(Brand, CategoryMobilephone).filter(
                db.and_(
                    CategoryMobilephone.brand_id==Brand.id,CategoryMobilephone.id.in_(phone_ids.keys())
                )).all()
            phone_attributes = self.dump_attributes([], phones, phone_ids)
            result = product_schema.dump(phone_attributes).data

        if len(game_machine_ids) > 0:
            game_machine = db.session.query(Brand, CategoryGameMachine).filter(
                db.and_(
                    CategoryGameMachine.brand_id==Brand.id,CategoryGameMachine.id.in_(game_machine_ids.keys())
                )).all()
            game_machine_attributes = self.dump_attributes([], game_machine, game_machine_ids)
            result = result + product_schema.dump(game_machine_attributes).data
        return {'status': 'success', 'data': result}, 200

    def update(self, method):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        shoplist_count_schema = ShoplistCount()
        data, errors = shoplist_count_schema.load(json_data)
        if errors:
            return errors, 422
        if method == 'post':
            exsits_count = ShopCart.get_count(data['uid'], data['key'])
            counts = int(exsits_count) +data['nums']
        elif method == 'put':
            counts = data['nums']
        if  data['nums'] < 0:
            return {'message': 'Cannot add number below zero'}, 400
        elif data['nums'] > 99:
            return {'message': 'The maximum limit is 99'}, 400
        elif counts > data['remain_count']:
            return {'message': 'Can not exceed the stock number'}, 400
        else:
            ShopCart.set_count(data['uid'], data['key'], counts)
        return { "status": 'success'}, 201

    def post(self):
        return self.update('post')

    def put(self):
        return self.update('put')
    
    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        shoplist_key_schema = ShoplistKey()
        data, errors = shoplist_key_schema.load(json_data)
        if errors:
            return errors, 422
        ShopCart.del_record(data['uid'], data['key'])
        return { "status": 'success'}, 200


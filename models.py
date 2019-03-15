from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

#category
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.CHAR(20), unique=True, nullable=False)
    sub_table_name = db.Column(db.CHAR(50), unique=True, nullable=False)

class CategorySchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)

#products
class CategoryMobilephone(db.Model):
    __tablename__ = 'category_mobilephone'
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id', ondelete='CASCADE'), nullable=False)
    memory = db.Column(db.Integer)
    color = db.Column(db.CHAR(10)) 
    price = db.Column(db.Numeric(10,2))
    add_time = db.Column(db.Integer)
    remain_count = db.Column(db.Integer, nullable=False)

class CategoryGameMachine(db.Model):
    __tablename__ = 'category_game_machine'
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id', ondelete='CASCADE'), nullable=False)
    disk = db.Column(db.Integer)
    memory = db.Column(db.Integer) 
    color = db.Column(db.CHAR(10))
    joy_stick_num = db.Column(db.Integer)
    price = db.Column(db.Numeric(10,2))
    add_time = db.Column(db.Integer)
    remain_count = db.Column(db.Integer, nullable=False)

class ProductSchema(ma.Schema):
    id = fields.Integer()
    brand_id = fields.Integer(required=True)
    price = fields.Float(required=True)
    remain_count = fields.Integer(required=True)
    logo = fields.String()
    brand_name = fields.String()
    category = fields.Integer()
    num = fields.Integer()

#brand
class Brand(db.Model):
    __tablename__ = 'brand'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Integer, db.ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    logo = db.Column(db.String(1024), nullable=False)


#user
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))

#shoplistCount sechema
class ShoplistCount(ma.Schema):
    uid = fields.Integer(required=True)
    key = fields.String(required=True)
    nums = fields.Integer(required=True)
    remain_count = fields.Integer(required=True)

class ShoplistKey(ma.Schema):
    uid = fields.Integer(required=True)
    key = fields.String(required=True)
rom flask import Flask
from flask_restful import Resource, Api 

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {"id": "2", "title": "switch8", "price": "300"}

api.add_resource(Product, '/')

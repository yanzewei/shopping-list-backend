from flask_redis import FlaskRedis
from flask import Flask

redis_store = FlaskRedis()

class Shoplist():
    @staticmethod
    def get_by_uid(uid):
        app = Flask(__name__)
        app.config.from_object("config")
        redis_store.init_app(app, decode_responses=True)
        return redis_store.hgetall('shopping_nums_u'+str(uid))
        #print(redis_store.hget("shopping_nums_u1"))

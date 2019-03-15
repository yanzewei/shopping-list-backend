from flask_redis import FlaskRedis
from flask import Flask

redis_store = FlaskRedis()
app = Flask(__name__)
app.config.from_object("config")
redis_store.init_app(app, decode_responses=True)

class Shoplist():
    @staticmethod
    def get_by_uid(uid):
        return redis_store.hgetall('shopping_nums_u'+str(uid))
        #print(redis_store.hget("shopping_nums_u1"))
    @staticmethod
    def set_count(uid, field, nums):
        hash_key = 'shopping_nums_u'+str(uid)
        return redis_store.hset(hash_key, field, nums)
    @staticmethod
    def get_count(uid, field):
        hash_key = 'shopping_nums_u'+str(uid)
        if redis_store.hexists(hash_key, field) == 1:
            count = redis_store.hget(hash_key, field)
            return int(count)
        else:
            return 0
    @staticmethod
    def del_record(uid, field):
        hash_key = 'shopping_nums_u'+str(uid)
        return redis_store.hdel(hash_key, field)
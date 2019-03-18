from flask import Flask
from flask_cors import CORS
from config import config
import os
from dotenv import find_dotenv,load_dotenv

def create_app(config_filename):
    app = Flask(__name__)
    CORS(app)
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    config_obj = config[os.getenv('FLASK_CONFIG') or 'default']
    app.config.from_object(config_obj)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from models import db
    db.init_app(app)

    from redismodels import redis_store
    redis_store.init_app(app, decode_responses=True)


    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)

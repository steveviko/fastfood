from flask import Flask
from .config import app_config
# from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)




def create_app():
    # Initialize flask app
    _app= Flask(__name__, instance_relative_config=True)    
    return _app


app = create_app()

# load from config.py in root folder
# app.config.from_object(app_config["development"])
# app.config['JWT_SECRET_KEY'] = 'thebreakthrough'
# jwt = JWTManager(app)

from .db import DatabaseConnection

# db = DatabaseConnection()
# db.create_user_table()
#db.create_orders_table()
# db.create_menu_table()
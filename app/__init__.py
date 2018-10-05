from flask import Flask
from flask_jwt_extended import(JWTManager,jwt_required,create_access_token,get_jwt_identity)


app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['JWT_SECRET_KEY']="breakthrough"
jwt =JWTManager(app)


from app.views import app

from .db import DatabaseConnection
  









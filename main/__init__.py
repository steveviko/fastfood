from flask import Flask
from .config import app_config





def create_app():
    # Initialize flask app
    _app= Flask(__name__, instance_relative_config=True)    
    return _app


app = create_app()
# load from config.py in root folder
app.config.from_object(app_config["development"])

from .db import DatabaseConnection
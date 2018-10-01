from flask import Flask


app = Flask(__name__)

from .db import DatabaseConnection
# db = DatabaseConnection()
# db.create_tables()
#from .request.views import post 
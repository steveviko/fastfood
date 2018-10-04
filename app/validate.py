from flask import request, jsonify
import re 
from werkzeug.security import generate_password_hash, check_password_hash

from app import app

class Validation:
    pass
import jwt
import json
import uuid
from datetime import datetime, timedelta
from flask import current_app


class User:

    """   Class to represent the User model    """

    def __init__(self, email, password, admin=False):
        self.id = uuid.uuid4().int
        self.email = email
        self.password =password
        self.registered_on = datetime.datetime.now()
        self.admin = admin


    def json(self):
        """  json representation of the User       """

        return json.dumps({
            'id': self.id,           
            'email': self.email,
            'password': self.password,
            'registered_on':self.registered_on,
            'admin':self.admin
        })

def generate_token(user_id):
    """Generates the access token to be used as the Authorization header"""

    try:
        # set up a payload with an expiration time
        payload = {
            'exp': datetime.utcnow() + timedelta(minutes=30),
            # international atomic time
            'iat': datetime.utcnow(),
            # default  to user id
            'sub': user_id
        }
        # create the byte string token using the payload and the SECRET key
        jwt_string = jwt.encode(
            payload,
            current_app.config.get('SECRET_KEY'),
            algorithm='HS256'
        ).decode('UTF-8')
        return jwt_string

    except Exception as e:
        # return an error in string format if an exception occurs
        return str(e)

def decode_token(token):
    """Decode the access token to get the payload and return user_id and isAdmin field results"""
    try:
        payload = jwt.decode(token, current_app.config.get('SECRET_KEY'))
        return {"id": payload['sub'], "status": "Success"}
    except jwt.ExpiredSignatureError:
        return {"status": "Failure", "message": "Expired token. Please log in to get a new token"}
    except jwt.InvalidTokenError:
        return {"status": "Failure", "message": "Invalid token. Please register or login"}
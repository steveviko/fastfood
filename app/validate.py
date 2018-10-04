import os
from flask import request, jsonify
import re 
from werkzeug.security import generate_password_hash, check_password_hash
from app import app
# from user import User
from .user_activities import UserActivities



activities = UserActivities()



class Validation:
    def validate_email(self,email):
        check_duplicate_email = activities.get_user(email)

        if check_duplicate_email > 0:
            return jsonify({'error': 'Sorry user already exists'}), 409
        elif len(email) < 6:
            return jsonify({'error': 'Email can not be less than six\
                characters'}), 400
        elif email.isdigit():
            return jsonify({'error': 'Email format not allowed\
            an email can not only have numbers'}), 400
        elif "@" not in email:
            return jsonify({'error': 'Email format not allowed\
            an email must conatain @'}), 400
        elif "." not in email:
            return jsonify({'error': 'Email format not allowed\
            an email must conatain . character'}), 400
        elif email.startswith("@") or email.startswith("."):
            return jsonify({'error': 'Email format not allowed\
            an email must not start with @ or . character'}), 400
        elif "@." in email:
            return jsonify({'error': 'Email format not allowed an email must not start with @ or .\
            character next to each other'}), 400
        elif ".@" in email:
            return jsonify({'error': 'Email format not allowed an email must not start with @ or .\
            character next to each other'}), 400
        

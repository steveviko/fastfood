from .user import User
from .db import DatabaseConnection,Users
from werkzeug.security import generate_password_hash, check_password_hash




class UserActivities:
    def __init__(self):
        self.datab = DatabaseConnection()
        self.db_user=Users()
        self.user_obj=User()

    
    def user_register(self, email, password):
        self.user_obj.email = email
        self.user_obj.password = password
        hash_password = generate_password_hash(self.user_obj.password, method='sha256')
        user_record =self.db_user.register_user(self.user_obj.email, self.user_obj.password, hash_password )
        print("user creation was successful")
        return {'user': user_record }

    
    def get_user(self, email):
        fetch = self.db_user.fetch_user(email)
        return fetch
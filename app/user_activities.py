from .user import User
from .db import DatabaseConnection
from werkzeug.security import generate_password_hash, check_password_hash

user = User()
datab= DatabaseConnection()

class UserActivities:
    
    def user_register(self, email, password):
        user.email = email
        user.password = password
        hash_password = generate_password_hash(user.password, method='sha256')
        user_record =datab.register_user(user.email, user.password, hash_password )
        print("user creation was successful")
        return {'user': user_record }

    def view_all_orders(self):
        return self.datab.get_orders()
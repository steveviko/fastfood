import re

from flask import Flask, jsonify, make_response,json, request

from  main.models.orders import Order
from app import create_app
from main.models.user import User

orders = Order()
users_list=[]


app = create_app()

@app.route("/api/v1/orders", methods =["GET"])
def get_all_orders():    
    if orders.order_list == []:
        return jsonify({"orders": "No orders Available"}), 400
    list_of_orders = orders.get_all()
    return jsonify({'orders': list_of_orders}), 200

@app.route("/api/v1/auth/login", methods =["POST"])
def signup(self):
    
    """
    Allows users(admins and customers) to create accounts        """
    # get the post data
    post_data = request.get_json()        
    email = post_data['email']
    password = post_data['password']
    

    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        return make_response(jsonify({"message": "Enter valid email"}), 400)

    if password.strip() == "":
        return make_response(jsonify({"message": "Enter password"}), 400)

    if len(password) < 5:
        return make_response(jsonify({"message": "Password is too short, < 5"}), 400)

    new_user = User(email, password)

    for user in users_list:
        if email == user['email']:
            return make_response(jsonify({"message": "email already in use"}), 400)

    users_list.append(json.loads(new_user.json()))
    return make_response(jsonify({'message': 'User successfully created', 'email': new_user.email}), 201)


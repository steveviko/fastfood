from flask import request, jsonify, make_response,json
from app import app
from app.db import DatabaseConnection,Order,Menu,Users
from app.validate import Validation
from .user_activities import UserActivities






orders = Order()
menus = Menu()
user = Users()
db=DatabaseConnection()
db.create_menu_table()
db.create_user_table()
db.create_orders_table()
validate = Validation()
activity = UserActivities()

@app.route('/api/v2/orders', methods=['POST'])
def create_order():
    data = request.data
    results  =json.loads(data)    
    amount = results['amount']
    ordered_at = results['ordered_at']
    status = results['status']
    insert_one= orders.post_order(amount, ordered_at,status)
    if insert_one == "":
        return jsonify({'order': insert_one})

@app.route("/api/v2/orders", methods=["GET"])
def get_all_orders():        
    order_list = orders.get_orders()
    return jsonify({'orders': order_list}), 200

@app.route('/api/v2/menu-items', methods=['POST'])
def create_menu():
    data = request.data
    results  =json.loads(data) 
    menu={   
    "item_name": results['item_name'],
    "amount":results['amount']
    }
    insert_menu= menus.add_menu_item(menu )
    return jsonify({'menu': insert_menu})  

@app.route("/api/v2/menu", methods=["GET"])
def get_all():
    """Implements the get menu api."""
    menu_items = menus.get_menu_items()
    return jsonify({'menu': menu_items}), 200

@app.route('/api/v2/auth/signup', methods=['POST'])
def register_user():
    request_data = request.data
    data = json.loads(request_data)
    if not data:
        return jsonify({'error': 'unsupported format'}), 400
    elif 'email' not in data:
        return jsonify({'error': 'user name is requred'}), 400
    elif 'password' not in data:
        return jsonify({'error': 'password required'}), 400
    email = data['email']
    password = data['password']
    if not validate.validate_email(email):
        activity.user_register(email, password)
        return jsonify({'success': 'registered successfully'}), 201
    else:
        return validate.validate_email(email)


@app.route("/api/v1/orders/<int:orderId>", methods =["GET"])
def get_one_order(orderId):
    if isinstance(orderId,int):
        single_order = orders.get_an_order(orderId)
        return jsonify({"order": single_order}),200
    else:
        return jsonify({"Message": " Error,Please fill out correct  id"}), 400
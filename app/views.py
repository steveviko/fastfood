from flask import request, jsonify, make_response,json

from app import app
from app.db import DatabaseConnection,Order,Menu,Users
from app.validate import Validation



orders = Order()
menus = Menu()
user = Users()
db=DatabaseConnection()
db.create_menu_table()
db.create_user_table()
db.create_orders_table()
validate = Validation()

@app.route('/api/v2/orders', methods=['POST'])
def create_order():
    data = request.data
    results  =json.loads(data)    
    amount = results['amount']
    ordered_at = results['ordered_at']
    status = results['status']
    insert_one= orders.post_order(amount, ordered_at,status)
    return jsonify({'order': insert_one})
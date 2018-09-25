from flask import Flask, jsonify, make_response,json, request

from app import create_app

from  .models.order import Order,Menu

orders = Order()
menus = Menu()




app = create_app()

@app.route("/api/v1/orders", methods =["GET"])
def get_all_orders():
    if orders.order_list == []:
        return jsonify({"orders": "No orders Available"}), 400
    list_of_orders = orders.get_all()
    return jsonify({'orders': list_of_orders}), 200

@app.route("/api/v1/orders/<int:orderId>", methods =["GET"])
def get_one_order(orderId):
    if isinstance(orderId,int):
        single_order = orders.get_order_by_id(orderId)
        return jsonify({"order": single_order}),200
    else:
        return jsonify({"Message": " Error,Please fill out correct  id"}), 400

@app.route("/api/v1/orders", methods =["POST"])
def post_order(): 
    request_data=request.data
    results  =json.loads(request_data)
    order = {
        "name": results["name"],
        "item": results["item"],
        "amount": results["amount"]
        
    }
    if order["name"] == "" or order["amount"] == "" or order["item"] == "":
        return jsonify({"message": "Error,order is not complete "}), 400
    else:
        orders.add(order)
        return jsonify({'Order': order }), 201

@app.route("/api/v1/orders/<int:orderId>", methods = ["PUT"])
def Edit_order(orderId):
    request_data=request.data
    results  =json.loads(request_data)
    order_status = results["status"]
    updates = orders.update_order(int(orderId), order_status)
    return jsonify({"order": updates}), 201






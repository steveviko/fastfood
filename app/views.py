from flask import Flask, jsonify, make_response, redirect, json, Response, request,abort

from app import create_app

from  .models.order import FastFoodOrders



orders = FastFoodOrders()

app = create_app()

@app.route("/api/v1/orders", methods =["GET"])
def get_all_orders():
    return orders.get_all()

@app.route("/api/v1/orders/<int:orderId>", methods =["GET"])
def get_one_order(orderId):
    return orders.get_order_by_id(orderId)

@app.route("/api/v1/orders", methods =["POST"])
def post_order():
    request_data = request.get_json()
    if not validate_order(request_data):
        name = request_data['name']
        desc = request_data['description']
        return jsonify(orders.add_orders(name, desc)), 201
    

def validate_order(request_object):
    if not request_object:
        abort(400)
    if 'name' not in request_object:
        return {'error': 'please name is required'}
    if 'desc' not in request_object:
        return {'error': 'please description is required'}


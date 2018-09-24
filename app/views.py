from flask import Flask, jsonify, make_response,json, request

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
   return orders.add_orders()
    




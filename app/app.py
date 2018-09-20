from flask import Flask,jsonify, request, json,abort

from model import FastFoodOrders

order = FastFoodOrders()

app = Flask(__name__)

@app.route("/api/v1/orders", methods =["POST"])
def create_order():
    return order.add_order()

@app.route("/api/v1/orders", methods =["GET"])
def get_all_orders():
    return order.get_all()


@app.route("/api/v1/orders/<int:orderId>", methods = ["GET"])
def get_order_by_id(orderId):
    return order.get_id(orderId)

@app.route("/api/v1/orders/<int:orderId>", methods = ["PUT"])
def createA(orderId):
    return order.Edit_an_order(orderId)


if __name__=='__main__':
    app.run(debug=True)

from flask import Flask,jsonify, request, json,abort

from model import FastFoodOrders

order = FastFoodOrders()

app = Flask(__name__)

@app.route("/api/v1/orders", methods =["POST"])
def create_order():
    return order.add_order()


if __name__=='__main__':
    app.run(debug=True)
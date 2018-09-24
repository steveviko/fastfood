from flask import Flask, jsonify, request, json,Blueprint

listofOrders = []

class FastFoodOrders(object):
   
    def __init__(self):        
        self.order_id = None
        self.name = None
        self.description = None
        
  
    def get_all(self):
        """This endpoint will fetch all orders """
        listofOrders = []
        if listofOrders == []:
            return jsonify({"message":"The orders list is currently empty"}), 404
        for order in listofOrders:           
            listofOrders.append(order)
        return jsonify(listofOrders), 200
        
    def get_order_by_id(self,orderId):
        orders =[order for order in listofOrders if order['id']== orderId]
        if  orders:
            return jsonify({'order':orders[0]}), 200 
        return jsonify({"message": "The order does not exist "}), 404

    def add_orders(self,name,description):
        """This endpoint will add an order """
        self.name = name
        self.description = description
        data= [order for order in listofOrders if order['name'] ==self.name]
        if len(self.name) < 2:
            return {'error': 'order name can not be less than two characters'}       
        if self.name.isdigit():
            return {'error': 'name format not allowed'}
       
        if data:
            return {'error': 'order already exists'}
        if not listofOrders:
            self.order_id = 1
        else:
            self.order_id = listofOrders[-1]['order_id'] + 1
        order = {
            'order_id': self.order_id,
            'name': self.name,
            'description': self.description
        }
        listofOrders.append(order)
        return order          
                    
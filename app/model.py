from flask import Flask, jsonify, request, json,abort


class FastFoodOrders():
    def __init__(self):
        self.listofOrders =[]
  

    def add_order(self):              
        data= request.data
        results  =json.loads(data)      
        self.listofOrders.append(results) 
        if not results:              
            return "No value found"  
        return jsonify(self.listofOrders)

    def get_all(self):
        if self.listofOrders:
            return jsonify(self.listofOrders)
        else:
            return jsonify({'messsage':'orders is Currently Empty'})

    def get_id(self,orderId):
        orders =[order for order in self.listofOrders if order['id']== orderId]
        if orders:
            return jsonify({'order':orders[0]})
        else:
            return jsonify({'Error':'Id not found'})
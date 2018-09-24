from flask import Flask, jsonify, request, json,Blueprint



class FastFoodOrders():
   
    def __init__(self):        
        self.listofOrders = []
        
  
    def get_all(self):
        """This endpoint will fetch all orders """
        listofOrders = []
        if listofOrders == []:
            return jsonify({"message":"The orders list is currently empty"}), 404
        for order in listofOrders:           
            listofOrders.append(order)
        return jsonify(listofOrders), 200
        
    def get_order_by_id(self,orderId):
        orders =[order for order in self.listofOrders if order['id']== orderId]
        if  orders:
            return jsonify({'order':orders[0]}), 200 
        return jsonify({"message": "The order does not exist "}), 404

    def add_orders(self):
        data= request.data
        results  =json.loads(data)      
        self.listofOrders.append(results) 
        if not results:              
            return "No value found"  
        return jsonify(self.listofOrders)
            
                    
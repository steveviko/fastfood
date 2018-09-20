from flask import Flask, jsonify, request, json


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
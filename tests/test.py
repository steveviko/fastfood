import unittest
import json
from app.models.order import Order
from app.views import app



class TestQuestion(unittest.TestCase): 
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.order = Order()
        self.sample_order= {
           'id': 1,
            'name': 'All Food',
            'amount': '23,000',
            'item': 4,
            'status': 'Pending'
        }
            

        

    def test_order_creation(self):
         self.assertIsInstance(self.order, Order)

    def test_add(self):
        response = self.app.post("/api/v1/orders", data = json.dumps(self.sample_order), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_orders(self):
        response = self.app.get("/api/v1/orders")
        self.assertEqual(response.status_code, 200)

    def test_get_single_order(self):
        response = self.app.get("/api/v1/orders/1")
        self.assertEqual(response.status_code, 200)
        
    def test_Edit_order(self):
       
        response = self.app.put("api/v1/orders/1", data = json.dumps(self.sample_order), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
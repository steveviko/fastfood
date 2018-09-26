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
            
        self.sample_menu = {
            "id": 1,
            "name": "Beef",
            "amount": 10000
        }
        

    def test_order_creation(self):
         """ test if object created is of class Order """ 
         self.assertIsInstance(self.order, Order)

    def test_add(self):
        self.assertEqual(len(self.order.order_list),0)
        self.order.add(self.sample_order)
        self.assertEqual(len(self.order.order_list),1)
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

    def test_add_menu(self):
        self.assertEqual(len(self.order.menu_item_list),0)
        self.order.add_menu_item(self.sample_menu)
        self.assertEqual(len(self.order.menu_item_list),1)
        response = self.app.post("/api/v1/menu-lists", data = json.dumps(self.sample_menu), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_fetch_all_menu(self):        
        self.assertEqual(len(self.order.menu_item_list),2)
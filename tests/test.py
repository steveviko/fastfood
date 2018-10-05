import unittest
from app.db import DatabaseConnection,Users,Menu,Order
from app import app

db = DatabaseConnection()
user =Menu()
order=Order()



class TestMainTestCase(unittest.TestCase): 
    def setUp(self):
        self.db= DatabaseConnection()
        self.menu =Menu()
        self.order=Order()

    def test_order_creation(self):
         """ test if object created is of class Order """ 
         self.assertIsInstance(self.order, Order)

    def test_menu_creation(self):
         """ test if object created is of class Order """ 
         self.assertIsInstance(self.menu, Menu)
   
    
        
    



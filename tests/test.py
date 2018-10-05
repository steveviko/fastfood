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
         """ test if object created is of class Menu """ 
         self.assertIsInstance(self.menu, Menu)
   
    def test_db_creation(self):
         """ test if object created is of class DatabaseConnection """ 
         self.assertIsInstance(self.db, DatabaseConnection)

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'breakthrough')
        self.assertTrue(app.config['TESTING'] is True)
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(app is None)
        
    def create_app(self):
        app.config.from_object('FASTFOOD.app.config.DevelopmentConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'breakthrough')
        self.assertTrue(app.config['DEBUG'])
    



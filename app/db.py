import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash




class DatabaseConnection:
        def __init__(self):
                """Connect to fastfood database."""
                self.connection = psycopg2.connect("dbname=fastfood user=manager password=fastadmin host=localhost")
                self.connection.autocommit = True
                self.cur = self.connection.cursor()
                self.dict_cursor=self.connection.cursor(cursor_factory=RealDictCursor)

                print("Connection to the db was a success")

        def create_user_table(self):

                """Create table to store users data."""
                user_table= ("CREATE TABLE IF NOT EXISTS users"
                        "(user_id serial  NOT NULL PRIMARY KEY,"                        
                        "username VARCHAR(50) UNIQUE NOT NULL,"
                        "Email VARCHAR(80) UNIQUE NOT NULL,"
                        "password VARCHAR(200) NOT NULL,"
                        "Role VARCHAR(10) NOT NULL)")

                self.cur.execute(user_table)

        def create_orders_table(self):
                """Create table for orders."""
                orders_table = ("CREATE TABLE IF NOT EXISTS orders"
                                "(order_id serial  NOT NULL PRIMARY KEY,"
                                "amount INTEGER NOT NULL,"
                                "ordered_at VARCHAR(25) NOT NULL,"
                                "status VARCHAR(11) NOT NULL,"
                                "user_id INTEGER, FOREIGN KEY (user_id) REFERENCES users(user_id),"
                                "menu_id INTEGER, FOREIGN KEY (menu_id) REFERENCES menu(menu_id))")
                self.cur.execute(orders_table)

        def create_menu_table(self):
                """Create table to store menu items."""
                menu_table = ("CREATE TABLE IF NOT EXISTS menu"
                                "(menu_id serial NOT NULL PRIMARY KEY,"
                                "item_name VARCHAR(60) UNIQUE NOT NULL,"
                                "Amount INTEGER NOT NULL)")
                self.cur.execute(menu_table)
    

class Users(DatabaseConnection):
    def check_user(self, account):
        sql = "SELECT username,password,role from users WHERE username= '{}'".format(account["username"])
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data


    

    def register_user(self, email, password, hash_password):
      
        """ insert a new user into the users table """
        sql = """INSERT INTO users(email, password, hash_password)
                VALUES(%s,%s, %s);"""
        return self.cur.execute(sql, (email, password, hash_password))
        
      
   
      
class Menu(DatabaseConnection):
    """Class for menu object."""
    def add_menu_item(self, menu):
        """ add items to menu."""
        
        for k, v in menu.items():
            if k == "amount":
                menu[k] = int(v)

        sql = "INSERT INTO menu(item_name, amount) VALUES (%s, %s)"
        self.cur.execute(sql, (menu["item_name"], menu["amount"]))

    def get_menu_items(self):
        """collect menu records  """
        sql = "SELECT * FROM menu"
        self.cur.execute(sql)
        menu = self.cur.fetchall()
        return menu 


    def check_exist(self, menu):
        sql = "SELECT item_name FROM menu WHERE item_name = '{}'".format(menu["item_name"])
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

class Order(Menu):  

    def add_orders(self, order,user_id):
        """Adding  orders."""
        for k, v in order.items():
            order[k] = int(v)
        sql="INSERT INTO orders(amount, ordered_at, status, user_id, menu_id) VALUES(\
        %s, NOW(), %s, %s, %s)"
        self.cur.execute(sql,(order["amount"], "Pending", user_id, order["item"]))
        return order
    

    def get_orders(self):
        """get all orders """
        sql="SELECT order_id, amount, status,ordered_at, item_name, username FROM orders \
        INNER JOIN menu ON orders.menu_id = menu.menu_id INNER JOIN users ON orders.user_id = users.user_id"
        self.cur.execute(sql) 
        result=self.cur.fetchall()     
        return result  

    def get_an_order(self, orderId):
        """get a specific record from  orders table."""
        sql = "SELECT * FROM orders WHERE order_id ='{}'".format(orderId)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

    def post_order(self, amount, ordered_at,status):        
        sql = "Insert INTO orders (amount, ordered_at,status) VALUES({},{},'{}')".format(
            amount, ordered_at,status)
        self.cur.execute(sql)
        

    def update_order_status(self, orderId, status):
        """Updates order status"""
        sql = "UPDATE orders SET status='{}' WHERE order_id ='{}'".format(status,orderId)
        self.cur.execute(sql)
        returned_status = "SELECT * FROM orders WHERE order_id = '{}'".format(orderId)
        self.cur.execute(returned_status)
        result = self.cur.fetchall()
        return result

    def check_exist(self, Order):
        sql = "SELECT item FROM order WHERE item = '{}'".format(Order["item"])
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result   

  
   
   
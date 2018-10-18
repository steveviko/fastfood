from flask import Flask, jsonify, request, json
from main.db import DatabaseConnection



class Order(DatabaseConnection):
    db = DatabaseConnection
    cursor = db.cur
    user_list =[]
    def __init__(self):
        pass
    def add_user(self, email,password,registered_on,admin):
       
        ''' add user to table '''
        sql = """INSERT INTO users(email,password,registered_on,admin) 
        VALUES('%s,%s,DEFAULT,False') """,
        (email,password,registered_on)
        self.cursor.execute(sql)
        self.con.commit()

    def get_all(self):

        '''Query data from the  table'''
        sql="select * from orders"
        self.cursor.execute(sql)
        records =self.cursor.fetchall()

        for record in records:
            return jsonify({"orders":record})

    def fetch_one(self):
        pass
       

    


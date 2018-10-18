import psycopg2


class DatabaseConnection():

    
    con =None

    try:
        # myConnection  to the db
        con = psycopg2.connect(host="localhost", user="manager",password="fastadmin", dbname="fastfood")
        print('connection to db was a success')

        commands = (
                """
                CREATE TABLE IF NOT EXISTS Users(
                    id SERIAL PRIMARY KEY,                                            
                    email VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    registered_on VARCHAR(255) NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    admin BOOLEAN NOT NULL DEFAULT FALSE
                
                )
                """,
                """ CREATE TABLE  IF NOT EXISTS orders(
                        id SERIAL PRIMARY KEY, 
                        item VARCHAR(255) NOT NULL,               
                        status VARCHAR(255) NOT NULL                  
                        
                        )
                """,
                """
                CREATE TABLE  IF NOT EXISTS category (
                        id INTEGER PRIMARY KEY,
                        name VARCHAR(255) NOT NULL
                    
                )
                """,
                """
                CREATE TABLE  IF NOT EXISTS item (
                        id INTEGER PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        description VARCHAR(255)  NOT NULL,
                        item_category VARCHAR(255)  NOT NULL,
                        amount VARCHAR(255)  NOT NULL               
                      
                    
                )
                """)
    
        
        
        cur = con.cursor()

        # create table one at a time
        for command in commands:
            cur.execute(command)
        # close communication with the fastfood database server
        cur.close()
        # commit the changes
        con.commit()
        

    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if con is not None:
            con.close()

    
    def add_user(self, email,password,registered_on,admin):
       
        ''' add user to table '''
        sql = """INSERT INTO users(email,password,registered_on,admin) 
        VALUES('%s,%s,DEFAULT,False') """,
        (email,password,registered_on)
        
        try:

            cur = self.con.cursor()
            # execute the INSERT statement
            cur.execute(sql)
             # commit the changes to the db
            self.con.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def add_order(self, item,status="pending"):
            ''' add order to table '''
            sql = """INSERT INTO orders(item,status) 
            VALUES('%s,DEFAULT') """,(item,status)
            try:
                cur = self.con.cursor()
                # execute the INSERT statement
                cur.execute(sql)
                # commit the changes to the db
                self.con.commit()
                # close communication with the database
                cur.close()

               
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

    def add_menu(self, name,amount=0):
            ''' add order to table '''
            sql = """INSERT INTO orders(item,amount) 
            VALUES('%s,DEFAULT') """, (name,amount)
            
            try:
                cur = self.con.cursor()
                # execute the INSERT statement
                cur.execute(sql)
                # commit the changes to the db
                self.con.commit()
                # close communication with the database
                cur.close()

               
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
   
  
   
   
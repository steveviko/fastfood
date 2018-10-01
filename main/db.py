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

    
        
            

   
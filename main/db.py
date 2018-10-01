import psycopg2


class DatabaseConnection():
    con =None

    try:
        # myConnection 
        con = psycopg2.connect(host="localhost", user="manager",password="fastadmin", dbname="fastfood")
        print('connection to db was a success')
        
    except:
        print('failed to connect to db')

    
        
            

   
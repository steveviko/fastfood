import psycopg2


class DatabaseConnection:
    def __init__(self):
        self.hostname = 'localhost'
        self.username = 'manager'
        self.password = 'fastadmin'
        self.database = 'fastfood'

        try:
            #print "Using psycopg2…"
            self.myConnection = psycopg2.connect( host=self.hostname, user=self.username, password=self.password, dbname=self.database )
            
        except:
            print('failed to connect to db')


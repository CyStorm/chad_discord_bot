from mysql.connector.connection import MySQLConnection

class DbConnection():
    def __init__(self, mysql_connection: MySQLConnection):
        self.connection= mysql_connection

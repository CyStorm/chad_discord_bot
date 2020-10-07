from mysql import connector


#TODO remove when done testing 
from mysql import connector
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_NAME = "discord_bot"
DB_USER = "root"
DB_PASSWORD = "Chad1234_"

class MySqlDbConnection():

    def __init__(self):
        self.connection = connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def execute_sql_command(self, command):
        self.cursor.execute("USE {}".format(DB_NAME))
        self.cursor.execute(command)


if __name__ == "__main__":
    # cnt = connector.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD)
    actual = MySqlDbConnection()
    actual.execute_sql_command("CREATE TABLE members")
'''MySQL database need to be setup
'''

from mysql import connector
from CONSTANTS import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER, DB_PORT

class MySqlDbConnection():

    def __init__(self):
        self.connection = connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD)
        self.cursor = self.connection.cursor()
        self.db_name = DB_NAME 

    def __del__(self):
        self.connection.close()

    def execute_sql_command(self, command):
        self.cursor.execute("USE {}".format(self.db_name))
        self.cursor.execute(command)
        self.connection.commit()

    def insert_to_table(self, table, columns, values):
        command = "INSERT INTO {table} {columns} VALUES {values}".format(table=table, columns=columns, values=values)
        self.execute_sql_command(command)

    def read_from_table(self, table, row, column, value):
        pass



if __name__ == "__main__":
    # cnt = connector.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD)
    actual = MySqlDbConnection()
    # actual.execute_sql_command("CREATE TABLE members")
    print(actual.insert_to_table("members", ("global_id", "display_name", "smooth)_"), "someval"))
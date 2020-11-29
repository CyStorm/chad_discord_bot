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

    def execute_sql_command(self, command: str):
        '''TODO cannot call this for all commands, need to make sure cursor object and commit commands are proper
        maybe even have a different one of this for modifying and non modifying sql queueys 
        '''
        cursor = self.connection.cursor()
        cursor.execute("USE {}".format(self.db_name))
        cursor.execute(command)
        self.connection.commit()
        #TODO need to do something with the cursor, fetch rows, or close it maybe yeild the cursor

    def dict_to_equalstr_with_sep(self, input_dict: dict, separator: str):
        '''Formats python dictionary into key = value strings with separtor
        '''
        result_list = []
        for key, val in input_dict.items():
            if (isinstance(val, str)):
                val = "'{}'".format(val)
            result_list.append("{} = {}".format(key, val))
        result_str = separator.join(result_list)
        return result_str

    def insert_in_table(self, table: str, columns: tuple, values: tuple):
        '''Inserts into database table
        '''
        col_str = str(columns).replace("'", "")
        val_str = str(values)
        command = "INSERT INTO {table} {columns} VALUES {values}".format(table=table, columns=col_str, values=val_str)
        self.execute_sql_command(command)

    def update_to_table(self, table: str, update_dict: dict, condition_dict: dict):
        update_str = self.dict_to_equalstr_with_sep(update_dict, ", ")
        condition_str = self.dict_to_equalstr_with_sep(condition_dict, " AND ")
        command = "UPDATE {table} SET {update} WHERE {condition}".format(table=table, update=update_str, condition=condition_str)
        self.execute_sql_command(command)

    def read_from_table(self):
        pass

if __name__ == "__main__":
    # cnt = connector.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD)
    actual = MySqlDbConnection()
    # actual.execute_sql_command("CREATE TABLE members")
    test = {
        "global_id": 999,
        "display_name": "op",
        "smooth_counter": 9
    }

    cond = {
        "global_id": 1111
    }
    # print(actual.insert_in_table("members", ("global_id", "display_name", "smooth_counter"), (2231, "chad", 0)))
    # print(actual.dict_to_equalstr_with_sep(test, ", "))
    # actual.execute_sql_command("INSERT INTO members (global_id, display_name, smooth_counter) VALUES (222, 'chad', 22)
    a = actual.execute_sql_command("SELECT * FROM members")
    print(a)
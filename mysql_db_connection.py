'''MySQL database need to be setup
'''

from mysql import connector


class MySqlDbConnection():

    def __init__(self, db_name, host, user, password):
        self.connection = connector.connect(host=host, user=user, password=password)
        self.db_name = db_name

    def __del__(self):
        self.connection.close()

    def execute_sql_no_return(self, command: str):
        '''TODO cannot call this for all commands, need to make sure cursor object and commit commands are proper
        maybe even have a different one of this for modifying and non modifying sql queueys
        '''
        cursor = self.connection.cursor()
        cursor.execute("USE {}".format(self.db_name))
        cursor.execute(command)
        self.connection.commit()
        cursor.close()
        # TODO need to do something with the cursor, fetch rows, or close it maybe yeild the cursor

    def execute_sql_with_return(self, command: str):
        cursor = self.connection.cursor(dictionary=True, buffered=True)
        cursor.execute("USE {}".format(self.db_name))
        cursor.execute(command)
        result = cursor.fetchall()
        cursor.close()
        return result

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

    def insert_in_table(self, table: str, columns_tup: tuple, values_tup: tuple):
        '''Inserts into database table
        '''
        col_str = str(columns_tup).replace("'", "")
        val_str = str(values_tup)
        command = "INSERT INTO {table} {columns} VALUES {values}".format(table=table, columns=col_str, values=val_str)
        print(self.execute_sql_no_return(command))

    def update_to_table(self, table: str, update_dict: dict, condition_dict: dict):
        update_str = self.dict_to_equalstr_with_sep(update_dict, ", ")
        condition_str = self.dict_to_equalstr_with_sep(condition_dict, " AND ")
        command = "UPDATE {table} SET {update} WHERE {condition}".format(table=table, update=update_str, condition=condition_str)
        self.execute_sql_no_return(command)

    def read_from_table(self, table: str, columns_tup: tuple, condition_dict: dict):
        col_str = ", ".join(columns_tup)
        cond_str = self.dict_to_equalstr_with_sep(condition_dict, " AND ")
        command = "SELECT {column} FROM {table} WHERE {condition}".format(table=table, column=col_str, condition=cond_str)
        return self.execute_sql_with_return(command)

    def read_all_from_table(self, table: str, condition_dict):
        cond_str = self.dict_to_equalstr_with_sep(condition_dict, " AND ")
        command = "SELECT * FROM {table} WHERE {condition}".format(table=table, condition=cond_str)
        return self.execute_sql_with_return(command)

    def get_colum_names(self, table: str):
        command = "SHOW COLUMNS FROM {}".format(table)
        result = self.execute_sql_with_return(command)
        return_list = []
        for column in result:
            return_list.append(column["Field"])
        print(return_list)
        return tuple(return_list)

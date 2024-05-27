import pandas as pd
from .constants import Constants
class SQLGenerator:

    #defaults if not specified


    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.dataframe = None

    def load_csv(self):
        # converts all values to string so processing can be done on the warehouse side
        self.dataframe = pd.read_csv(self.csv_file_path, dtype=str)

    def create_temp_table_sql(self, table_name, column_type):
        if self.dataframe is None:
            raise ValueError("Dataframe is not loaded. Call load_csv() first.")
        
        columns = self.dataframe.columns
        column_definitions = ",\n\t".join([f"\"{col.strip()}\" {column_type}" for col in columns])
        
        create_table_query = (
            f"CREATE TEMP TABLE {table_name} (\n"
            f"\t{column_definitions}\n"
            ");"
        )
        return create_table_query.strip()

    def insert_data_sql(self, table_name, rows):
        if self.dataframe is None:
            raise ValueError("Dataframe is not loaded. Call load_csv() first.")
        
        insert_statements = []
        counter = 1
        total_rows = self.dataframe.shape[0]
        if rows == None:
            rows = total_rows
        for _, row in self.dataframe.iterrows():
            columns = ', '.join(self.dataframe.columns)
            values = ', '.join([f"'{str(value).strip()}'" if not pd.isna(value) else 'NULL' for value in row])
            if counter == total_rows:
                punctuation = ";"
            else:
                punctuation = ','
            if counter == 1:
                insert_clause = f"INSERT INTO {table_name} VALUES"
                insert_statements.append(insert_clause)
            insert_statement = f"\t({values}){punctuation}"
            insert_statements.append(insert_statement)
            counter += 1
        return insert_statements

    def generate_sql(self, table_name, column_type, rows):
        self.load_csv()
        if table_name == None:
            table_name = Constants.DEFAULT_TABLE_NAME
        if column_type == None:
            column_type = Constants.DEFAULT_COLUMN_TYPE
        create_table_sql = self.create_temp_table_sql(table_name, column_type)
        insert_data_sql = self.insert_data_sql(table_name, rows)
        return create_table_sql, insert_data_sql


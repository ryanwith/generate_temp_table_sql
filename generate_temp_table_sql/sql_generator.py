import pandas as pd

class SQLGenerator:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.dataframe = None

    def load_csv(self):
        self.dataframe = pd.read_csv(self.csv_file_path)

    def create_temp_table_sql(self, table_name='temp_table'):
        if self.dataframe is None:
            raise ValueError("Dataframe is not loaded. Call load_csv() first.")
        
        columns = self.dataframe.columns
        # Join columns with a newline and tab for better formatting
        column_definitions = ",\n\t".join([f"{col.strip()} TEXT" for col in columns])
        
        create_table_query = (
            f"CREATE TEMP TABLE {table_name} (\n"
            f"\t{column_definitions}\n"
            ");"
        )
        return create_table_query.strip()
        
    def insert_data_sql(self, table_name='temp_table'):
        if self.dataframe is None:
            raise ValueError("Dataframe is not loaded. Call load_csv() first.")
        
        insert_statements = []
        counter = 1
        total_rows = self.dataframe.shape[0]
        for _, row in self.dataframe.iterrows():
            columns = ', '.join(self.dataframe.columns)
            values = ', '.join([f"'{str(value)}'" for value in row])
            if counter == total_rows:
                punctuation = ";"
            else:
                punctuation = ','
            if counter == 1:
                insert_statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values}){punctuation}"
            else:
                insert_statement = f"({values}){punctuation}"
            insert_statements.append(insert_statement)
            counter = counter + 1
        return insert_statements

    def generate_sql(self, table_name='temp_table'):
        self.load_csv()
        create_table_sql = self.create_temp_table_sql(table_name)
        insert_data_sql = self.insert_data_sql(table_name)
        return create_table_sql, insert_data_sql


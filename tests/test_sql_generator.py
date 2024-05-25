import unittest
import os
from generate_temp_table_sql.sql_generator import SQLGenerator

class TestSQLGenerator(unittest.TestCase):
    def setUp(self):
        # Path to the test data file
        self.csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'test_data.csv')
        self.sql_generator = SQLGenerator(self.csv_file_path)
    
    def test_load_csv(self):
        self.sql_generator.load_csv()
        self.assertIsNotNone(self.sql_generator.dataframe)
        self.assertEqual(list(self.sql_generator.dataframe.columns), ['name', 'age', 'city'])
        self.assertEqual(len(self.sql_generator.dataframe), 2)
    
    def test_create_temp_table_sql(self):
        self.sql_generator.load_csv()
        create_table_sql = self.sql_generator.create_temp_table_sql('test_table')
        expected_sql = (
            "CREATE TEMP TABLE test_table (\n"
            "\tname TEXT,\n"
            "\tage TEXT,\n"
            "\tcity TEXT\n"
            ");"
        )
        self.assertEqual(create_table_sql, expected_sql)
    
    def test_insert_data_sql(self):
        self.sql_generator.load_csv()
        insert_data_sql = self.sql_generator.insert_data_sql('test_table')
        expected_sql = [
            "INSERT INTO test_table (name, age, city) VALUES\n\t('John', '30', 'New York'),",
            "\t('Jane', '25', 'Los Angeles');"
        ]
        self.assertEqual(insert_data_sql, expected_sql)
    
    def test_generate_sql(self):
        self.sql_generator.load_csv()
        create_table_sql, insert_data_sql = self.sql_generator.generate_sql('test_table')
        
        expected_create_table_sql = (
            "CREATE TEMP TABLE test_table (\n"
            "\tname TEXT,\n"
            "\tage TEXT,\n"
            "\tcity TEXT\n"
            ");"
        )
        expected_insert_data_sql = [
            "INSERT INTO test_table (name, age, city) VALUES\n\t('John', '30', 'New York'),",
            "\t('Jane', '25', 'Los Angeles');"
        ]
        
        self.assertEqual(create_table_sql, expected_create_table_sql)
        self.assertEqual(insert_data_sql, expected_insert_data_sql)
    
if __name__ == '__main__':
    unittest.main()
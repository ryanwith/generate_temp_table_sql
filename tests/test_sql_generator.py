import unittest
import os;
from generate_temp_table_sql.sql_generator import SQLGenerator

class TestSQLGenerator(unittest.TestCase):
    def setUp(self):
        self.csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'test_data.csv')
        self.sql_generator = SQLGenerator(self.csv_file_path)
    
    def test_load_csv(self):
        self.sql_generator.load_csv()
        self.assertIsNotNone(self.sql_generator.dataframe)
    
    def test_create_temp_table_sql(self):
        self.sql_generator.load_csv()
        create_table_sql = self.sql_generator.create_temp_table_sql('test_table')
        self.assertIn('CREATE TEMP TABLE', create_table_sql)
    
    def test_insert_data_sql(self):
        self.sql_generator.load_csv()
        insert_data_sql = self.sql_generator.insert_data_sql('test_table')
        self.assertTrue(len(insert_data_sql) > 0)
        self.assertIn('INSERT INTO test_table', insert_data_sql[0])
    
    def test_generate_sql(self):
        create_table_sql, insert_data_sql = self.sql_generator.generate_sql('test_table')
        self.assertIn('CREATE TEMP TABLE', create_table_sql)
        self.assertTrue(len(insert_data_sql) > 0)
        self.assertIn('INSERT INTO test_table', insert_data_sql[0])
    
if __name__ == '__main__':
    unittest.main()

import unittest
import os
from generate_temp_table_sql.sql_generator import SQLGenerator
from generate_temp_table_sql.constants import Constants

class TestSQLGenerator(unittest.TestCase):
    def setUp(self):
        # Path to the test data file
        self.csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'test_data.csv')
        self.sql_generator = SQLGenerator(self.csv_file_path)
    
    def test_load_csv(self):
        self.sql_generator.load_csv()
        self.assertIsNotNone(self.sql_generator.dataframe)
        self.assertEqual(list(self.sql_generator.dataframe.columns), ['name', 'age', 'current city'])
        self.assertEqual(len(self.sql_generator.dataframe), 2)
    
    def test_create_temp_table_sql(self):
        self.sql_generator.load_csv()
        create_table_sql = self.sql_generator.create_temp_table_sql('test_table1', 'STRING')
        expected_sql = (
            "CREATE TEMP TABLE test_table1 (\n"
            "\t\"name\" STRING,\n"
            "\t\"age\" STRING,\n"
            "\t\"current city\" STRING\n"
            ");"
        )
        self.assertEqual(create_table_sql, expected_sql)
    
    def test_insert_data_sql(self):
        self.sql_generator.load_csv()
        insert_data_sql = self.sql_generator.insert_data_sql('test_table1', None)
        expected_sql = [
            "INSERT INTO test_table1 VALUES",
            "\t('John', '30', 'New York'),",
            "\t('Jane', '25', 'Los Angeles');\n"
        ]
        self.assertEqual(insert_data_sql, expected_sql)
    
    def test_generate_sql_with_custom_values(self):
        self.sql_generator.load_csv()
        create_table_sql, insert_data_sql = self.sql_generator.generate_sql('test_table1', 'STRING', None)
        
        expected_create_table_sql = (
            "CREATE TEMP TABLE test_table1 (\n"
            "\t\"name\" STRING,\n"
            "\t\"age\" STRING,\n"
            "\t\"current city\" STRING\n"
            ");"
        )
        expected_insert_data_sql = [
            "INSERT INTO test_table1 VALUES",
            "\t('John', '30', 'New York'),",
            "\t('Jane', '25', 'Los Angeles');\n"
        ]
        
        self.assertEqual(create_table_sql, expected_create_table_sql)
        self.assertEqual(insert_data_sql, expected_insert_data_sql)

    def test_generate_sql_with_batch_size(self):
        self.sql_generator.load_csv()
        create_table_sql, insert_data_sql = self.sql_generator.generate_sql(None, None, 1)
        
        expected_create_table_sql = (
            "CREATE TEMP TABLE table_name (\n"
            "\t\"name\" TEXT,\n"
            "\t\"age\" TEXT,\n"
            "\t\"current city\" TEXT\n"
            ");"
        )
        expected_insert_data_sql = [
            "INSERT INTO table_name VALUES",
            "\t('John', '30', 'New York');\n",
            "INSERT INTO table_name VALUES",
            "\t('Jane', '25', 'Los Angeles');\n"
        ]
        
        self.assertEqual(create_table_sql, expected_create_table_sql)
        self.assertEqual(insert_data_sql, expected_insert_data_sql)


    def test_default_table_name_and_column_type(self):
        self.sql_generator.load_csv()
        create_table_sql, insert_data_sql = self.sql_generator.generate_sql(None, None, None)
        
        expected_create_table_sql = (
            f"CREATE TEMP TABLE {Constants.DEFAULT_TABLE_NAME} (\n"
            f"\t\"name\" {Constants.DEFAULT_COLUMN_TYPE},\n"
            f"\t\"age\" {Constants.DEFAULT_COLUMN_TYPE},\n"
            f"\t\"current city\" {Constants.DEFAULT_COLUMN_TYPE}\n"
            ");"
        )
        expected_insert_data_sql = [
            f"INSERT INTO {Constants.DEFAULT_TABLE_NAME} VALUES",
            "\t('John', '30', 'New York'),",
            "\t('Jane', '25', 'Los Angeles');\n"
        ]
        
        self.assertEqual(create_table_sql, expected_create_table_sql)
        self.assertEqual(insert_data_sql, expected_insert_data_sql)

    def test_empty_csv(self):
        self.csv_file_path_empty = os.path.join(os.path.dirname(__file__), 'data', 'empty.csv')
        sql_generator_empty = SQLGenerator(self.csv_file_path_empty)
        sql_generator_empty.load_csv()
        
        create_table_sql = sql_generator_empty.create_temp_table_sql('test_table', 'TEXT')
        expected_create_table_sql = (
            "CREATE TEMP TABLE test_table (\n"
            "\t\"name\" TEXT,\n"
            "\t\"age\" TEXT,\n"
            "\t\"current city\" TEXT\n"
            ");"
        )
        
        insert_data_sql = sql_generator_empty.insert_data_sql('test_table', None)
        expected_insert_data_sql = []
        
        self.assertEqual(create_table_sql, expected_create_table_sql)
        self.assertEqual(insert_data_sql, expected_insert_data_sql)

    def test_nan_values(self):
        self.csv_file_path_with_nan = os.path.join(os.path.dirname(__file__), 'data', 'test_data_with_nan.csv')
        sql_generator_with_nan = SQLGenerator(self.csv_file_path_with_nan)
        sql_generator_with_nan.load_csv()
        
        insert_data_sql = sql_generator_with_nan.insert_data_sql('test_table', None)
        expected_sql = [
            "INSERT INTO test_table VALUES",
            "\t('John', '30', 'New York'),",
            "\t('Jane', NULL, 'Los Angeles');\n"
        ]
        
        self.assertEqual(insert_data_sql, expected_sql)


if __name__ == '__main__':
    unittest.main()
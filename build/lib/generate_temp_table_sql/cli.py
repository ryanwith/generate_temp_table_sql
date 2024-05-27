import argparse
import os
from generate_temp_table_sql.sql_generator import SQLGenerator

def main():
    parser = argparse.ArgumentParser(description='Process a CSV file to generate SQL statements.')
    parser.add_argument('csv_file', type=str, help='The path to the CSV file')
    parser.add_argument('-o', '--output_file', type=str, help='The path to the output SQL file.  Defaults to the director you call the command in.')
    parser.add_argument('--overwrite', action='store_true', help='Allow overwriting the output file if it exists')
    parser.add_argument('--table_name', type=str, help='The name of the temp table you will create')
    parser.add_argument('--column_type', type=str, help='The data type of the columns in the temp table.  Defaults to TEXT which works for Redshift and Snowflake.  BigQuery requires STRING.')
    parser.add_argument('--batch_size', type=int, help='The number of rows inserted per insert statement.  If present, it creates multiple insert statements based on the batch size specified.')

    args = parser.parse_args()
    
    # Use specified output file name or generate a default one
    if args.output_file is None:
        base_name = os.path.splitext(os.path.basename(args.csv_file))[0]
        args.output_file = os.path.join(os.getcwd(), base_name + '_temp_table.sql')

    # Check if the file exists and handle accordingly
    if os.path.exists(args.output_file) and not args.overwrite:
        print(f"Error: The file '{args.output_file}' already exists. Use --overwrite to allow overwriting.")
        return

    sql_generator = SQLGenerator(args.csv_file)
    
    sql_generator.load_csv()
    
    create_table_sql, insert_data_sql = sql_generator.generate_sql(args.table_name, args.column_type, args.batch_size)
    
    with open(args.output_file, 'w') as f:
        f.write("--Create Table SQL:\n")
        f.write(create_table_sql + "\n\n")
        f.write("--Insert Data SQL:\n")
        for query in insert_data_sql:
            f.write(query + "\n")

    print(f"SQL statements successfully written to {args.output_file}")

if __name__ == '__main__':
    main()

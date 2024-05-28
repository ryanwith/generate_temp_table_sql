# Generate Temp Table SQL

Generate Temp Table SQL is a Python package that generates SQL statements for creating a temporary table and inserting data from a CSV file.  It's useful when you need to move data between disconnected databases and data warehouses.  You can now simply unload a CSV, turn that CSV into SQL statements creating a temp table and inserting data with a CLI command, and copy those SQL statements into your query editor so you can start using the data in a different warehouse.

<b>Why did I build this?</b>  I'm often wondering how a product I'm working on is linked to customer spend.  However, my operational warehouse that includes data like the dates and times customers used a product is separate from my financial warehouse which has the billing data.  I need to move data from one to the other so I can join the finance and product data together to do an analysis...and turning the CSV into SQL by hand in excel is a PITA.  With this, I can now move the data in seconds.  I simply download the CSV, run <code>generate-tt-sql csv_name.csv</code> in my terminal, and copy it into my query editor.  It's immediately available to query so I can go straight to analysis.

## Features

- Load data from a CSV file
- Generate a `CREATE TEMP TABLE` SQL statement
- Generate `INSERT INTO` SQL statements for the data
- Command-line interface (CLI) for easy usage

## Installation

### Prerequisites

- Python 3.6 or higher
- `pandas` library

### Installing

1. Clone the repository:
    ```sh
    git clone https://github.com/rywaldor/generate_temp_table_sql.git
    cd generate_temp_table_sql
    ```

2. Install the package locally:
    ```sh
    pip install -e .
    ```

## Usage

### Command-Line Interface (CLI)

After installing the package, you can use the `generate-tt-sql` command to generate SQL statements from a CSV file.

#### Basic Usage

To generate SQL statements and save them to a file:
```sh
generate-tt-sql path/to/your/file.csv
```

#### Additional Options
```sh

--o The path to the output SQL file.  Defaults to the director you call the command in.
--overwrite: Allow overwriting the output file if it exists.
--table_name: Specify the name of the temporary table to create.
--column_type: Specify the data type of the columns in the temporary table. Defaults to TEXT which works for Redshift and Snowflake. Use STRING for BigQuery.
```

#### Example
Assume you have a CSV file example.csv with the following content:

```sh
name,age,city
John,30,New York
Jane,25,Los Angeles
```

Run the following command to generate SQL statements:

```sh
generate-tt-sql example.csv -o output.sql --table_name my_temp_table --column_type STRING
```

The output.sql file will contain:

```sh
CREATE TEMP TABLE my_temp_table (
    name STRING,
    age STRING,
    city STRING
);

--Insert Data SQL:
INSERT INTO my_temp_table (name, age, city) VALUES 
    ('John', '30', 'New York'),
    ('Jane', '25', 'Los Angeles');
```

#### Running Tests
To run the tests, use the following command:

```sh
python -m unittest discover -s tests
```

#### Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (git checkout -b feature-branch)
3. Commit your changes (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature-branch)
5. Create a new Pull Request

#### License
This project is licensed under the MIT License - see the LICENSE file for details.

#### Author
Ryan Waldorf - ryan@ryanwaldorf.com<br/>
<a href="https://github.com/ryanwaldorf" target="_blank">GitHub</a>
<a href="https://www.linkedin.com/in/ryan-waldorf/" target="_blank">LinkedIn</a>
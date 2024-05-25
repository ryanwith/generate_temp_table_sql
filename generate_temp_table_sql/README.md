# Generate Temp Table SQL

Generate Temp Table SQL is a Python package that generates SQL statements for creating a temporary table and inserting data from a CSV file.

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
    git clone https://github.com/yourusername/generate_temp_table_sql.git
    cd generate_temp_table_sql
    ```

2. Install the package locally:
    ```sh
    pip install -e .
    ```

## Usage

### Command-Line Interface (CLI)

After installing the package, you can use the `generate-sql` command to generate SQL statements from a CSV file.

#### Basic Usage

To generate SQL statements and save them to a file:
```sh
generate-sql path/to/your/file.csv -o path/to/output/file.sql

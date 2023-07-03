def generate_sql_code():
    # Prompt for database name
    database_name = input("Enter Database name: ")

    # Prompt for dimension table details
    num_tables = int(input("Enter the number of dimension tables: "))

    dimension_tables = []
    for i in range(1, num_tables + 1):
        table_name = input(f"Enter Table {i} name: ")
        columns = input(f"Enter Table {i} columns (comma-separated): ").split(",")
        primary_key = input(f"Enter Table {i} primary key: ")

        # Prompt for column data types
        column_types = {}
        for column in columns:
            column_type = input(f"Enter data type for {column}: ")
            column_types[column] = column_type

        dimension_table = {
            "name": f"dim_{table_name}",
            "primary_key": primary_key,
            "columns": columns,
            "column_types": column_types
        }

        dimension_tables.append(dimension_table)

    # Prompt for fact table details
    fact_table_name = input("Enter Fact Table name: ")
    surrogate_key_name = input("Enter Surrogate Key name: ")
    fact_table_columns = input("Enter Fact Table columns (comma-separated): ").split(",")

    # Prompt for schema name or use default schema if not provided
    schema_name = input("Enter Schema name (leave blank for default schema): ")
    if schema_name:
        schema_prefix = f"{schema_name}."
    else:
        schema_prefix = ""

    # Generate SQL code
    sql_code = ""

    # Create Dimension Tables
    for dimension_table in dimension_tables:
        table_name = dimension_table["name"]
        primary_key = dimension_table["primary_key"]
        columns = dimension_table["columns"]
        column_types = dimension_table["column_types"]

        # Drop table if it exists
        sql_code += f"DROP TABLE IF EXISTS {database_name}.{schema_prefix}{table_name};\n"

        # Create table
        sql_code += f"CREATE TABLE {database_name}.{schema_prefix}{table_name} (\n"
        for column in columns:
            column_type = column_types[column]
            sql_code += f"  {column} {column_type},\n"
        sql_code += f"  PRIMARY KEY ({primary_key})\n"
        sql_code += ");\n\n"

    # Create Fact Table
    sql_code += f"DROP TABLE IF EXISTS {database_name}.{schema_prefix}{fact_table_name};\n"
    sql_code += f"CREATE TABLE {database_name}.{schema_prefix}{fact_table_name} (\n"
    sql_code += f"  {surrogate_key_name} INT IDENTITY (1, 1) PRIMARY KEY,\n"  # Surrogate Key
    for dimension_table in dimension_tables:
        dimension_table_name = dimension_table["name"]
        dimension_primary_key = dimension_table["primary_key"]
        sql_code += f"  {dimension_primary_key} INT,\n"  # Foreign Key column in the fact table

    for column in fact_table_columns:
        column_type = input(f"Enter data type for {column}: ")
        sql_code += f"  {column} {column_type},\n"

    # Add foreign key constraints
    for dimension_table in dimension_tables:
        dimension_table_name = dimension_table["name"]
        dimension_primary_key = dimension_table["primary_key"]
        constraint_name = f"FK_{dimension_table_name}"

        sql_code += f"  CONSTRAINT {constraint_name} FOREIGN KEY ({dimension_primary_key}) REFERENCES {database_name}.{schema_prefix}{dimension_table_name}({dimension_primary_key}),\n"

    sql_code = sql_code.rstrip(",\n")  # Remove the trailing comma and newline
    sql_code += "\n);"

    # Print the generated SQL code
    # print("\nGenerated SQL Code:\n")
    return sql_code



if __name__ =="__main__":
    generate_sql_code()

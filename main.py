from code_generator import generate_sql_code
from sql_writer import write_sql_code_to_file

# Call the function to generate SQL code
sql_code = generate_sql_code()

# Prompt for the filename
file_name = input("Enter the filename: ")

# Write the SQL code to the file
write_sql_code_to_file(sql_code, file_name)

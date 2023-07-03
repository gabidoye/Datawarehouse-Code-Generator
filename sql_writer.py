def write_sql_code_to_file(sql_code, file_name):
    file_path = file_name + '.sql'
    with open(file_path, 'w') as file:
        file.write(sql_code)
    print("SQL code has been successfully written to the file:", file_path)

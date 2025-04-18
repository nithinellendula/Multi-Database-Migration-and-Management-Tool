def get_datatype(dest_db, datatype):
    dt = datatype.lower()
    # Convert for destination MySQL
    if dest_db == 1:
        if 'int' in dt or 'number' in dt:
            return 'INT'
        elif 'char' in dt or 'text' in dt or 'varchar2' in dt:
             'VARCHAR(255)'
        elif 'date' in dt:
            return 'DATE'
        elif 'float' in dt or 'double' in dt or 'numeric' in dt:
            return 'FLOAT'
        else:
            return 'VARCHAR(255)'
    # Convert for destination PostgreSQL
    elif dest_db == 3:
        if 'int' in dt or 'number' in dt:
            return 'INTEGER'
        elif 'char' in dt or 'text' in dt or 'varchar2' in dt:
            return 'TEXT'
        elif 'date' in dt:
            return 'DATE'
        elif 'float' in dt or 'double' in dt or 'numeric' in dt:
            return 'NUMERIC'
        else:
            return 'TEXT'
    # Convert for destination Oracle
    elif dest_db == 2:
        if 'int' in dt or 'integer' in dt:
            return 'NUMBER'
        elif 'char' in dt or 'text' in dt or 'varchar' in dt:
            return 'VARCHAR2(255)'
        elif 'date' in dt or 'timestamp' in dt:
            return 'DATE'
        elif 'float' in dt or 'numeric' in dt:
            return 'FLOAT'
        else:
            return 'VARCHAR2(255)'
    return 'VARCHAR(255)'
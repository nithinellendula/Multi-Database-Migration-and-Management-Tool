from utils.logger import get_logger

logger = get_logger("schema")

def get_table_schema(src, cursor, table):
    try:
        logger.info(f"Fetching schema for table '{table}' from DB {src}")
        if src == 1:
            cursor.execute(f"DESCRIBE {table}")
            schema = [(col[0], col[1]) for col in cursor.fetchall()]
        elif src == 3:
            cursor.execute(f"""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name = '{table}' AND table_schema = 'public';
            """)
            schema = cursor.fetchall()
        elif src == 2:
            cursor.execute(f"""
            SELECT column_name, data_type
            FROM user_tab_columns
            WHERE table_name = UPPER('{table}')
            """)
            schema = cursor.fetchall()
        else:
            raise ValueError("Invalid source DB")
            logger.debug(f"Schema for '{table}': {schema}")
            return schema
    except Exception as e:
        logger.error(f"Error fetching schema: {e}")
        raise
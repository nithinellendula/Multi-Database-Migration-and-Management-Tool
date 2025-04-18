from utils.logger import get_logger

logger = get_logger("Tables")

def get_available_tables(db_type, cursor):
    """
    Fetches the available tables from a database based on the db_type.
    Args:
    - db_type (int): Database type identifier (1: MySQL, 2: Oracle, 3: PostgreSQL)
    - cursor: Database cursor object to execute SQL queries.
    Returns:
    - list: List of available table names in the database.
    """
    try:
        if db_type == 1: # MySQL
            logger.info("Fetching available tables from MySQL...")
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            logger.debug(f"Fetched {len(tables)} tables from MySQL.")
        elif db_type == 2: # Oracle
            logger.info("Fetching available tables from Oracle...")
            cursor.execute("SELECT table_name FROM user_tables")
            tables = cursor.fetchall()
            logger.debug(f"Fetched {len(tables)} tables from Oracle.")
        elif db_type == 3: # PostgreSQL
            logger.info("Fetching available tables from PostgreSQL...")
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
            tables = cursor.fetchall()
            logger.debug(f"Fetched {len(tables)} tables from PostgreSQL.")
        else:
            logger.error("Invalid database type provided!")
            raise ValueError("Unsupported DB type! Please provide a valid DB type (1 for MySQL, 2 for Oracle, 3 for PostgreSQL).")
        # If no tables are found, log a warning
        if not tables:
            logger.warning("No tables found in the specified database.")
            return [table[0] for table in tables] # Return only table names (assuming table is a tuple)
    except Exception as e:
        logger.error(f"Error fetching tables from database (DB Type: {db_type}): {e}")
        raise
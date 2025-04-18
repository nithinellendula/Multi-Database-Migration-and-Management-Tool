import mysql.connector as my
import psycopg2 as pg
import cx_Oracle as cx
from .schema import get_table_schema
from .datatype_mapper import get_datatype
from utils.logger import get_logger

logger = get_logger("operations")

def create_table(dest_cursor, table_name, schema, dest_db):
    try:
        logger.info(f"Creating table '{table_name}' in DB {dest_db}")
        columns = []
        for col_name, data_type in schema:
            mapped_type = get_datatype(dest_db, data_type)
            columns.append(f"{col_name} {mapped_type}")
        create_query = f"CREATE TABLE {table_name} ({', '.join(columns)})"
        logger.debug(f"Executing query: {create_query}")
        dest_cursor.execute(create_query)
        logger.info(f"Table '{table_name}' created successfully.")
    except Exception as e:
        logger.error(f"Failed to create table '{table_name}': {e}")
        raise

def insert_data(db, db_conn,db_cur, tbl, data):
    cnt = db_conn
    try:
        # Step 1: Fetch schema and columns
        schema = get_table_schema(db, db_cur, tbl)
        col_names = [col[0] for col in schema]
        logger.info(f"Detected columns for table '{tbl}': {col_names}")
        # Step 2: Prepare dynamic query
        columns_str = ", ".join(col_names)
        if db == 2:
            placeholders = ", ".join([f":{i+1}" for i in range(len(col_names))])
        else:
            placeholders = ", ".join(["%s"] * len(col_names))
            query = f"INSERT INTO {tbl} ({columns_str}) VALUES ({placeholders})"
            logger.debug(f"Constructed INSERT query: {query}")
            # Step 3: Insert rows one by one
            for row in data:
                logger.debug(f"Inserting row: {row}")
                db_cur.execute(query, row)
            # Step 4: Commit the transaction
            cnt.commit()
            logger.info(f"Successfully inserted {len(data)} rows into table '{tbl}'.")
    except (my.Error, cx.Error, pg.Error) as e:
        logger.error(f"Database error while inserting into '{tbl}': {e}", exc_info=True)
        cnt.rollback()
        logger.warning(f"Transaction rolled back for table '{tbl}' due to error.")

def select_data(cursor, table_name):
    try:
        logger.info(f"Selecting data from table '{table_name}'")
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        results = cursor.fetchall()
        logger.debug(f"Fetched {len(results)} rows from '{table_name}'")
        return results
    except Exception as e:
        logger.error(f"Error selecting data from '{table_name}': {e}")
        raise
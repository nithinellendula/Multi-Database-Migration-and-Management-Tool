from database.operations import select_data,insert_data
from utils.input_utils import get_table_name
from utils.logger import get_logger

logger = get_logger("transfer")

def data_transfer(s,s_cur, d, d_conn,d_cur, table):
    tbl= table
    logger.info(f"Starting data transfer: {tbl} from DB {s} to DB {d}")
    # Fetch data from source database
    src = select_data(s_cur, tbl)
    if src is None:
        logger.info("Data not fetched")
    else:
        logger.debug(f"Fetched data: {src}") # Debug: Print the data being fetched
    # Insert data into destination database
    insert_data(d, d_conn,d_cur, tbl, src)
    # Query the destination table to confirm the transfer
    transferred_data = select_data(d_cur, tbl)
    if transferred_data:
        print(f"Transferred Data from {tbl}:")
        for row in transferred_data:
            print(row)
    else:
        logger.warning("No data found in the destination table.")
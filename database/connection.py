from utils.logger import get_logger
import mysql.connector as my
import psycopg2 as pg
import cx_Oracle as cx

logger = get_logger("connection")

def mysql_connect(config):
    try:
        logger.info("Connecting to MySQL...")
        conn = my.connect(**config)
        logger.info("MySQL connection established.")
        return conn
    except Exception as e:
        logger.error(f"MySQL connection failed: {e}")
        raise

def postgres_connect(config):
    try:
        logger.info("Connecting to PostgreSQL...")
        conn = pg.connect(**config)
        logger.info("PostgreSQL connection established.")
        return conn
    except Exception as e:
        logger.error(f"PostgreSQL connection failed: {e}")
        raise

def oracle_connect(config):
    try:
        logger.info("Connecting to Oracle...")
        conn = cx.connect(**config)
        logger.info("Oracle connection established.")
        return conn
    except Exception as e:
        logger.error(f"Oracle connection failed: {e}")
        raise
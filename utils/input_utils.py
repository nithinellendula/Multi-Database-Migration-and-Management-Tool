# utils/input_utils.py
from utils.logger import get_logger

logger = get_logger("input_utils")

def get_db_choice(prompt):
    try:
        choice = int(input(prompt))
        logger.info(f"User selected DB option: {choice}")
        return choice
    except ValueError as e:
        logger.error("Invalid input! Expected an integer.")
        raise

def get_action_choice():
    try:
        action = int(input("Enter action you want to perform:\n 1. Table Creation 2. Data Transfer :"))
        logger.info(f"User selected action: {action}")
        return action
    except ValueError as e:
        logger.error("Invalid input! Expected an integer.")
        raise

def get_table_name():
    table = input("Enter the table name: ").strip().lower()
    logger.info(f"User selected table: {table}")
    return table

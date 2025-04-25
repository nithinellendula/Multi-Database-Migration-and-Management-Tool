# Multi-Database Data Transfer Automation using Python

## Objective
Developed a Python script with a GUI interface using `tkinter` that automates data transfer between three different relational database management systems (RDBMS): MySQL, PostgreSQL, and Oracle. The script dynamically connects to the selected source and destination databases, fetches data from a table, and inserts it into the corresponding table in the destination database.

## Project Overview
This project is a modular, command-line-based Python application that facilitates
schema migration and data transfer between MySQL, PostgreSQL, and Oracle
databases. Designed for developers and DBAs, the tool automates schema fetching,
table creation, and data movement from one database to another — all while ensuring
robust error handling, connection abstraction, and dynamic data type mapping. It
automates the process of:
• Extracting schema information
• Creating tables
• Inserting data
-It can serve as a lightweight ETL utility or database structure replication assistant.
### 🛠 Features
- **Cross-Database Compatibility:** Supports MySQL, PostgreSQL, and Oracle
databases

- **Schema Extraction:** Automatically retrieves table schemas from source
databases

- **Dynamic Table Creation:** Generates CREATE TABLE statements compatible with
the destination database

- **Data Insertion:** Efficiently inserts data into destination tables, handling data type
mappings.

- **Data Selection:** Retrieves data from source tables for inspection or transfer.
  
- **Logging and Error Handling:** Comprehensive logging for operations and robust
error handling with transaction rollbacks.

- **Configure Database Connections:**
Navigate to the configs/ directory and configure the connection settings for
each supported database (mysql_config.py, oracle_config.py, postgres_confi).

- Utility Modules for extensibility and readability
### Databases Involved:
- **MySQL**: `student` table with preloaded data
- **PostgreSQL**: `employee` table with preloaded data
- **Oracle**: `user_table` with preloaded data

### Common Tables in Each Database:
- **MySQL**: `student(sid, sname, saddress, marks)`
- **PostgreSQL**: `employee(eid, ename, eaddress, salary)`
- **Oracle**: `user_table(u_id, uname, uaddress, user_contact)`

## Key Features:
- Supports three database types: **MySQL**, **PostgreSQL**, and **Oracle**
- Dynamic source and destination configuration through a GUI using `tkinter`
- Data fetching from the source database using parameterized `SELECT` queries
- Data insertion into the destination using parameterized `INSERT` queries with support for Oracle placeholder syntax
- Logs each row being inserted for debug/traceability
- Displays transferred data after completion for verification
- Handles database connection and operation errors gracefully

## Tools and Technologies:
- **Python 3**
- **tkinter** (for GUI)
- **mysql-connector-python**
- **cx_Oracle**
- **psycopg2**
- **VS Code (IDE)**

## File Structure:
Here is the structure of the project files:

Database_Migration/
├── configs/                          
│   ├── mysql_config.py              
│   ├── postgress_config.py          
│   └── oracle_config.py             
├── utils/                           
│   └── input_util.py   
│   └── logger.py  
├── database/                       
│   ├── available_tables.py         
│   ├── connection.py                 
│   ├── data_transfer.py              
│   ├── datatype_mapper.py           
│   ├── operations.py                 
│   ├── schema.py                                     
├── main.py                          
├── app.log                          
              

## Sample Workflow:
1. **Run the script**: Execute the `main.py` script to launch the Tkinter GUI.
2. **Select Databases**: Choose the source and destination databases (MySQL, PostgreSQL, or Oracle).
3. **Select Table**: Choose the table you want to transfer (e.g., `student`).
4. **Start Transfer**: The script fetches data from the source and inserts it into the destination.
5. **View Results**: The GUI shows the transferred data after completion and logs each insertion.

## Example Use Cases:
- Migrating data between legacy systems.
- Consolidating distributed data for reporting.
- Syncing data across dev/test/staging environments.

## Error Handling:
- Catches and logs database-specific errors (e.g., connection failures, SQL syntax errors).
- Validates database type inputs.
- Ensures connection and cursor cleanup with `finally` blocks.

## Challenges Solved:
- Dynamic handling of three different database APIs.
- Managing data type and syntax compatibility.
- Ensuring atomic operations with commits and rollbacks.

## Next Steps:
- Add CLI argument support for automation.
- Implement data validation before insertion.
- Extend to support schema migration and column mapping.
- Add logging to a file instead of the console output.

## Installation Instructions:
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/multi-database-data-transfer.git
    cd multi-database-data-transfer
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure to have the following database drivers installed:
    - `mysql-connector-python`
    - `cx_Oracle`
    - `psycopg2`

4. Set up database configuration files inside the `configs/` folder:
    - **mysql_config.py**: MySQL connection parameters
    - **postgress_config.py**: PostgreSQL connection parameters
    - **oracle_config.py**: Oracle connection parameters

5. Launch the GUI:
    ```bash
    python main.py
    ```

## 
**GitHub Repository:** https://github.com/nithinellendula/Databases-Integration.git

**Status:** Functional, tested across MySQL, PostgreSQL, and Oracle on localhost

**Author:** Nithin Ellendula


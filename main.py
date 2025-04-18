import tkinter as tk
from tkinter import messagebox, ttk

from configs.mysql_config import mysql_credentials
from configs.postgres_config import postgres_credentials
from configs.oracl_config import oracl_credentials

from database.connection import oracle_connect, mysql_connect, postgres_connect
from database.schema import get_table_schema
from database.datatype_mapper import get_datatype
from database.operations import create_table
from database.data_transfer import data_transfer
from database.available_tables import get_available_tables

from utils.logger import get_logger

logger = get_logger("GUI")

class DBTransferApp:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Database Transfer Tool")
        self.root.configure(bg='#f0f4f8')
        
        self.label_font=("Segoe UI", 10, 'bold')
        self.entry_font=("Segoe UI", 10)
        self.btn_font= ("Segoe UI", 10, 'bold')
        self.bg_color='#f0f4f8'
        
        frame=tk.Frame(root, bg=self.bg_color)
        frame.pack(padx=20, pady=20)
        
        self.src_db_label = tk.Label(frame, text="Multi-Database Migrator and Management Tool", fg='darkblue',font= ("Segoe UI", 14, 'bold'))
        self.src_db_label.grid(row=0, column=1, columnspan=2 , pady=5, sticky='e')
        
        # Source Database Selection
        self.src_db_label = tk.Label(frame, text="Select Source Database:", font=self.label_font)
        self.src_db_label.grid(row=2, column=0, padx=2, pady=5, sticky='e')
        self.src_db = ttk.Combobox(frame, values=["MySQL", "Oracle", "PostgreSQL"], font=self.entry_font)
        self.src_db.grid(row=2, column=1, padx=2, pady=5)
        
        # Destination Database Selection
        self.dest_db_label = tk.Label(frame, text="Select Destination Database:", font=self.label_font)
        self.dest_db_label.grid(row=2, column=3, padx=2, pady=5, sticky='e')
        self.dest_db = ttk.Combobox(frame, values=["MySQL", "Oracle", "PostgreSQL"], font=self.entry_font)
        self.dest_db.grid(row=2, column=4, padx=2, pady=5)
        
        # Action Selection
        self.action_label = tk.Label(frame, text="Select Action:", font=self.label_font)
        self.action_label.grid(row=4, column=0, padx=2, pady=5)
        self.action = ttk.Combobox(frame, values=["Table Creation", "Data Transfer"], font=self.entry_font)
        self.action.grid(row=4, column=1, padx=2, pady=5)
        
        # Table Name Input
        self.table_label = tk.Label(frame, text="Enter Table Name:", font=self.label_font)
        self.table_label.grid(row=6, column=0, padx=2, pady=5)
        self.table_name = tk.Entry(frame)
        self.table_name.grid(row=6, column=1, padx=2, pady=5)
        
        # Execute Button
        self.execute_button = tk.Button(frame, text="Execute", command=self.execute_action, font=self.btn_font, fg='black', bg='green')
        self.execute_button.grid(row=8, column=1, padx=10, pady=10)
        
        self.clear_button = tk.Button(frame, text="Clear", command=self.clear_inputs, font=self.btn_font, fg='black', bg='red')
        self.clear_button.grid(row=8, column=2, padx=3, pady=10)
        
        # Output Text Box
        self.output_text = tk.Text(frame, height=10, width=50)
        self.output_text.grid(row=10, column=1, padx=10, pady=10)

    def execute_action(self):
        src_db_type = self.src_db.current() + 1
        dest_db_type = self.dest_db.current() + 1
        action_type = self.action.current() + 1
        table = self.table_name.get().strip()
        try:
            if not (self.src_db.get() and self.dest_db.get() and self.action.get() and table):
                raise ValueError("All input fields must be filled.")
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))
            self.output_text.insert(tk.END, f"⚠️ {e}\n")
            return
        try:
            src_config = self.get_config(src_db_type)
            src_conn = self.get_conn(src_db_type, src_config)
            src_cur = src_conn.cursor()
            dest_config = self.get_config(dest_db_type)
            dest_conn = self.get_conn(dest_db_type, dest_config)
            dest_cur = dest_conn.cursor()
            if action_type == 1: # Table Creation
                schema = get_table_schema(src_db_type, src_cur, table)
                create_table(dest_cur, table, schema, dest_db_type)
                dest_conn.commit()
                self.output_text.insert(tk.END, f"Table '{table}' created successfully in destination database.\n")
            elif action_type == 2: # Data Transfer
                data_transfer(src_db_type, src_cur, dest_db_type, dest_conn, dest_cur,table)
                self.output_text.insert(tk.END, f"Data transferred successfully from '{table}'.\n")
            else:
                messagebox.showerror("Action Error", "Invalid action selected.")
        except Exception as e:
            logger.exception(f"An error occurred: {e}")
            messagebox.showerror("Error", str(e))
        finally:
            src_cur.close()
            src_conn.close()
            dest_cur.close()
            dest_conn.close()

    def clear_inputs(self):
        self.src_db.set('')
        self.dest_db.set('')
        self.action.set('')
        self.table_name.delete(0, tk.END)
        self.output_text.delete('1.0', tk.END)

    def get_config(self, db_type):
        if db_type == 1:
            return mysql_credentials
        elif db_type == 2:
            return oracl_credentials
        elif db_type == 3:
            return postgres_credentials
        else:
            raise ValueError("Invalid DB type")

    def get_conn(self, db_type, db_config):
        if db_type == 1:
            return mysql_connect(db_config)
        elif db_type == 2:
            return oracle_connect(db_config)
        elif db_type == 3:
            return postgres_connect(db_config)
        else:
            raise ValueError("Invalid DB Configuration")

if __name__ == "__main__":
    root = tk.Tk()
    app = DBTransferApp(root)
    root.mainloop()
import json
import sqlite3
from sqlite3 import Error

# polączenie z bazą danych
def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       print(f"Connected to {db_file}")
       return conn
   except Error as e:
       print(e)

   

# stworzenie nowej tabeli
def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)


create_todo_sql = """
    -- todo table
    CREATE TABLE IF NOT EXISTS todo (
        id integer PRIMARY KEY,
        title text NOT NULL,
        description text,
        done text
    );
    """
db_file = "todo.db"

conn = create_connection(db_file)
if conn is not None:
        
    execute_sql(conn, create_todo_sql)







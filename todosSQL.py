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
       return conn
   except Error as e:
       print(e)

   return conn

    
    
   

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


if __name__ == "__main__":
    

    create_todo_sql = """
    -- todo table
    CREATE TABLE IF NOT EXISTS todo (
        id integer PRIMARY KEY,
        title text NOT NULL,
        description text,
        done text,
        csrf_token text
    );
    """

    db_file = "todo.db"

    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_todo_sql)
        conn.close()





class TodosSQL:
    def __init__(self):
        """
        Query all rows in the table
        :param conn: the Connection object
        :return:
        """
        conn = create_connection("todo.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM todo")
        rows = cur.fetchall()
        #print(rows)
        self.todos = rows

    def all(self):
        """
        Query all rows in the table
        :param conn: the Connection object
        :return:
        """
        conn = create_connection("todo.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM todo")
        rows = cur.fetchall()
        return rows

    def get(self, id):
        return self.todos[id]

    def create(self, data):
        #data.pop('csrf_token')
        """
        Create a new projekt into the projects table
        :param conn:
        :param data:
        :return: data id
        """
        conn = create_connection("todo.db")
        sql = '''INSERT INTO todo(title, description, done, csrf_token)
                VALUES(?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid

    def update(self, id, data):
        data.pop('csrf_token')
        self.todos[id] = data
        

todos = TodosSQL()




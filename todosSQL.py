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


class TodosSQL:
    def __init__(self):
        conn = create_connection("todo.db")
        
    def all(self):
        conn = create_connection("todo.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM todo")
        rows = cur.fetchall()
        return rows

    def get(self, id):
        conn = create_connection("todo.db")
        cur = conn.cursor()
        qs = []
        values = ()
        query={'id': id}
        for k, v in query.items():
            qs.append(f"{k}=?")
            values += (v,)
        q = " AND ".join(qs)
        cur.execute(f"SELECT * FROM todo WHERE {q}", values)
        rows = cur.fetchall()
        print(rows)
        return rows

    def create(self, data):
         
        conn = create_connection("todo.db")
        sql = '''INSERT INTO todo(title, description, done, csrf_token)
                VALUES(?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid

    def update(self, id, data):
        conn = create_connection("todo.db")
        
        values = tuple(v for v in data.values())
        values += (id, )
        print(values)
        sql = f''' UPDATE todo
                SET title = ?, description = ?, done = ?, csrf_token = ?
                WHERE id = ?'''
        try:
            cur = conn.cursor()
            cur.execute(sql, values)
            conn.commit()
            print("OK")
        except sqlite3.OperationalError as e:
            print(e)
        
        

todos = TodosSQL()
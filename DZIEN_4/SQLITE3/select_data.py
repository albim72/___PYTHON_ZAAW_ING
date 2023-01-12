import sqlite3
from sqlite3 import Error
from conn import create_connection

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    
    rows = cur.fetchall()
    for row in rows:
        print(row)


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()
    for row in rows:
        print(row)
              
def select_task_by_priority(conn,priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority = ?",(priority,))

    rows = cur.fetchall()
    for row in rows:
        print(row)
        
def select():
    database = r"C:\sqlite\db\specbaza.db"
    conn = create_connection(database)
    with conn:
        print("1. Zadanie z filtowaniem po priorytecie...")
        select_task_by_priority(conn,1)
        print("2. ZWyświetlenie wszystkich zadań...")
        select_all_tasks(conn)
        
        
        

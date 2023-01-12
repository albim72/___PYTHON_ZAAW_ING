import sqlite3
from sqlite3 import Error
from conn import create_connection

def create_project(conn,project):
    sql = """
        INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?)
    """

    cur = conn.cursor()
    cur.execute(sql,project)
    conn.commit()
    return cur.lastrowid


def create_task(conn, task):
    sql = """
        INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?)
    """

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def insert():
    database = r"C:\sqlite\db\specbaza.db"
    conn = create_connection(database)
    with conn:
        project = ('Super Apka -> Python Analiza Danych','2022-03-04',"2023-12-17")
        project_id = create_project(conn,project)

        task_1 = ("Analiza wymagań dotyczących aplikacji.",1,1,project_id,'2022-03-24','2022-04-20')
        task_2 = ("Przygotowanie diagramów UML.",1,1,project_id,'2022-04-24','2022-05-16')

        create_task(conn,task_1)
        create_task(conn,task_2)

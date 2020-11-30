import sqlite3
from sqlite3 import Error

database = r"C:\Users\SpencerMensah\Documents\presh\main\pythonsqlite.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def setupMain():
    sql_create_user_table = """ CREATE TABLE IF NOT EXISTS user (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        password text NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_user_table)
    else:
        print("Error! cannot create the database connection.")

def create_user(conn, user):
    sql = ''' INSERT INTO user(id,name,password)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

def addUser(id,username,password):
    conn = create_connection(database)
    if conn is not None:
        user = (id,username,password);
        create_user(conn, user)
    else:
        print("Error! cannot create the database connection.")

def select_all_user():
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM user")

        rows = cur.fetchall()

        for row in rows:
            print(row)

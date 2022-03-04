import sqlite3
from sqlite3 import Error


def new_connection():
    conn=None;
    db_name="normanpd.db"
    try:
        conn=sqlite3.connect(db_name)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return(db_name)

if __name__=='__main__':
    new_connection()

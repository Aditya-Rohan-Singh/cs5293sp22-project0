import sqlite3
from sqlite3 import Error

def database_connect(db_name):
    conn=None;
    try:
        conn=sqlite3.Connection(db_name)
        return conn
    except Error as e:
        print(e)



def create_table(conn):
    table_sql="""create table incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT
    )
    """
    try:
        connection=conn.cursor()
        connection.execute(table_sql)
    except Error as e:
        print(e)




if __name__=='__main__':
    db_name="normanpd.db"
    conn=database_connect(db_name)
    create_table(conn)

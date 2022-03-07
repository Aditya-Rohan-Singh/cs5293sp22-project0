import sqlite3
from sqlite3 import Error
import csv


def createdb(db_name):
    conn=None;
    try:
        conn=sqlite3.Connection(db_name)
    except Error as e:
        print(e)

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
    conn.close()

def insert_data(db_name):
    conn=None;
    try:
        conn=sqlite3.Connection(db_name)
    except Error as e:
        print(e)

    data = open('extracted_data.csv','r')
    read_data=csv.DictReader(data)
    to_db = [(i['incident_time'], i['incident_number'], i['incident_location'], i['nature'], i['incident_ori']) for i in read_data]
    insert_statement = "insert into incidents (incident_time, incident_number, incident_location, nature, incident_ori) values (?,?,?,?,?)"
    try:
        connection=conn.cursor()
        #connection.execute()
        connection.executemany(insert_statement,to_db)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)


if __name__=='__main__':
    db_name="normanpd.db"
    createdb(db_name)
    insert_data(conn)

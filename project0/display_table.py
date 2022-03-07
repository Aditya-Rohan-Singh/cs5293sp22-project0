import sqlite3

def status(db_name):

    conn=None;
    conn=sqlite3.Connection(db_name)
    cursor = conn.cursor()

    select_statement = 'select nature, count(nature) from incidents group by nature order by nature ASC;'
    data_retrived = cursor.execute(select_statement).fetchall()
    return(data_retrived)
    conn.close()

if __name__ == '__main__':
    db_name='normanpd.db'
    status(db_name)


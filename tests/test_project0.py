import sys
import os.path
working_directory = os.getcwd()
project0_path = working_directory + '/project0'
sys.path.append(project0_path)
import project0
from project0 import project0
import pytest
import re
import sqlite3

@pytest.fixture()
def test_url():
    url='https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-21_daily_incident_summary.pdf'
    return(url)

def test_fetch_data(test_url):
    data=project0.fetch_data(test_url)
    assert len(data) == 374028

def test_extract_data(test_url):
    data=project0.fetch_data(test_url)
    extracted_data = project0.extract_data(data)
    current_folder=os.getcwd()
    path=current_folder+'/extracted_data.csv'
    assert len(extracted_data) == 318
    assert os.path.exists(path)

def test_create_table():
    db_name='normanpd.db'
    project0.createdb(db_name)
    current_folder=os.getcwd()
    path=current_folder+'/normanpd.db'
    assert os.path.exists(path)


def test_insert_table():
    db_name='normanpd.db'
    project0.insert_data(db_name)
    conn=sqlite3.Connection(db_name)
    conn1=conn.cursor()
    result=conn1.execute('select count(*) from incidents').fetchone()[0]
    conn.close()
    assert result == 317

def test_status():
    db_name='normanpd.db'
    data_retreived=project0.status(db_name)
    assert len(data_retreived) == 64

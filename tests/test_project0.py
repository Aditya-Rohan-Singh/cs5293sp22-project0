import sys
sys.path.append('/home/amadro/githubfiles/project0/cs5293sp22-project0/project0')
import project0
from project0 import project0
import pytest
import os.path
import re


@pytest.fixture()
def test_url():
    url='https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-21_daily_incident_summary.pdf'
    return(url)


def test_fetch_data(test_url):
    data=project0.fetch_data(test_url)
    assert len(data) == 374028

#@pytest.mark.parametrize("data",project0.fetch_data(test_url))
def test_extract_data(test_url):
    data=project0.fetch_data(test_url)
    extracted_data = project0.extract_data(data)
    assert len(extracted_data) == 318
    assert os.path.exists('/home/amadro/githubfiles/project0/cs5293sp22-project0/extracted_data.csv')

def test_create_table():
    db_name='normanpd2022-02-21.db'
    project0.createdb(db_name)
    assert os.path.exists('/home/amadro/githubfiles/project0/cs5293sp22-project0/normanpd2022-02-21.db')


def test_insert_table():
    db_name='normanpd2022-02-21.db'
    project0.insert_data(db_name)



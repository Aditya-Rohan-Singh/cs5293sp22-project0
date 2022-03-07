import pytest
import sys
sys.path.append('/home/amadro/githubfiles/project0/cs5293sp22-project0/project0')
print(sys.path)
import project0

url='https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-21_daily_incident_summary.pdf'
data = project0.fetch_data(url)
print(len(data))

@pytest.fixture()
def test_url():
    url='https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-21_daily_incident_summary.pdf'
    return(url)

#def test_fetch_data(test_url):
    #data=project0.fetch_data(url)
#    assert len(data) == 




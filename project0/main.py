

import argparse
#import project0
import extractdata
from extractdata import extract_data
import fetchdata
from fetchdata import fetch_data
import re
import create_table
from create_table import createdb, insert_data
import display_table
from display_table import status

def main(url):
    
    #Download data from Provided URL
    Incident_data_raw=fetch_data(url)

    #Extract data from the downloaded data and create csv file
    Extracted_data=extract_data(Incident_data_raw)

    #Create table and insert data
    url_date=re.search('https://www.normanok.gov/sites/default/files/documents/2022-02/(.+?)_daily_incident_summary.pdf',url).group(1)
    db_name = 'normanpd' + url_date + '.db'
    createdb(db_name)
    insert_data(db_name)

    #Retrive data and display
    final_data = status(db_name)
    for incident, number in final_data:
        print(incident,"|",number)

if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument("--incident_url", type=str, required=True,help="Incident summary url.")
        args = parser.parse_args()
        if args.incident_url:
            main(args.incident_url)

        



import argpass
import project0
import extractdata
from extractdata import extract_data
import fetchdata
from fetchdata import fetch_data


def main(url):
    
    #Download data from Provided URL
    Incident_data_raw=fetch_data(url)

    #Extract data from the downloaded data and create csv file
    Extracted_data=extract_data(Incident_data_raw)

    print(Extracted_data)


if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument("--incident_url", type=str, required=True,help="Incident summary url.")
        args = parser.parse_args()
        if args.incident_url:
            main(args.incident_incdident_url)

        

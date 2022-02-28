

import argpass
import project0



def main(url):
    
    #Download data from Provided URL
    Incident_data_raw=project0.fetchincidents(url)

if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument("--incident_url", type=str, required=True,help="Incident summary url.")
        args = parser.parse_args()
        if args.incident_url:
            main(args.incident_incdident_url)

import urllib.request
import tempfile
import PyPDF2
import csv
import re
import sqlite3
from sqlite3 import Error


def fetch_data(url):

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    return(data)

def extract_data(data):

    #Opening csv file to write data
    csv_file=open('extracted_data.csv','w')
    writer=csv.writer(csv_file)


    filepointer = tempfile.TemporaryFile()
    filepointer.write(data)
    filepointer.seek(0)

    #Reading the pdf
    pdfReader = PyPDF2.pdf.PdfFileReader(filepointer)
    pagecount = pdfReader.getNumPages()

    extracted_data=[]
    st="Data Not Found"

    for pagenum in range(0,pagecount):

        #Extracting Texts
        page1 = pdfReader.getPage(pagenum).extractText()
        page1 = re.sub(' \n','',page1)                  #To deal with address 2nd line

        #Convert PDF headers into database headers
        page1 = re.sub('Date / Time\nIncident Number\nLocation\nNature\nIncident ORI','incident_time\nincident_number\nincident_location\nnature\nincident_ori',page1)
        page1 = page1.split("\n")

        #Row counter and list initialization
        i=0
        row=[]
        for j in range(0,len(page1)):
            if (len(page1[j])==0):
                row.append(st)
            else:
                if(i==2):
                    if(re.match('OK\d{7}',page1[j]) or re.match('EMSSTAT',page1[j]) or re.match('1400\d',page1[j])):
                        row.append("No Data")                                           #Address column is empty
                        row.append("No Data")                                           #Nature Column is empty
                        row.append(page1[j])
                        i=5
                    else:
                        row.append(page1[j])
                        i=i+1
                else:
                    row.append(page1[j])
                    i=i+1
                if(i>=5):
                    extracted_data.append(row)
                    writer.writerow(row)
                    row=[]
                    i=0
    csv_file.close()
    return(extracted_data)


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
    conn=sqlite3.Connection(db_name)
    
    data = open('extracted_data.csv','r')
    read_data=csv.DictReader(data)
    to_db = [(i['incident_time'], i['incident_number'], i['incident_location'], i['nature'], i['incident_ori']) for i in read_data]
    insert_statement = "insert into incidents (incident_time, incident_number, incident_location, nature, incident_ori) values (?,?,?,?,?)"
    try:
        connection=conn.cursor()
        connection.executemany(insert_statement,to_db)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)

def status(db_name):
    conn=None;
    conn=sqlite3.Connection(db_name)
    cursor = conn.cursor()

    select_statement = 'select nature, count(nature) from incidents group by nature order by nature ASC;'
    data_retrived = cursor.execute(select_statement).fetchall()
    conn.close()
    return(data_retrived)

#if __name__ == '__main__':


import fetchdata
from fetchdata import fetch_data
import tempfile
import PyPDF2
import csv
import re

def extract_data():
    url = ("https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-03_daily_incident_summary.pdf")
    #Retriving data from url
    data=fetch_data(url)

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
        
        #Removing nextlines in Address column
        page1 = re.sub('\nHWY','HWY',page1)
        page1 = re.sub('\nRD','RD',page1)
        page1 = re.sub('\nblvd','blvd',page1)
        page1 = re.sub('\nst','st',page1)
        #page1 = re.sub('\n\d{3}[a-z]','',page1)
        page1 = page1.split("\n")



        i=0
        row=[]
        for j in range(0,len(page1)):
            if (len(page1[j])==0):
                row.append(st)
            else:
                if(i==2 or i==3):
                    if(re.match('OK\d{7}',page1[j]) or re.match('EMSSTAT',page1[j]) or re.match('1400\d',page1[j])):
                        row.append("No Data")                                           #Address column is empty
                        row.append("No Data")                                           #Nature Column is empty
                        row.append(page1[j])
                        i=5
                    else:
                        row.append(page1[j]) 
                else:
                    row.append(page1[j])
                
                i=i+1
                if(i>=5):
                    #extracted_data.append(row)
                    writer.writerow(row)
                    row=[]
                    i=0
    
    csv_file.close()
    #return(extracted_data)


if __name__=='__main__':
    extract_data()

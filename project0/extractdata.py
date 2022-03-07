import tempfile
import PyPDF2
import csv
import re

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


if __name__=='__main__':
    #Testing purpose function calls
    url = ("https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-03_daily_incident_summary.pdf")
    data=extract_data(url)

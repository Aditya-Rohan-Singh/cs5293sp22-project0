# cs5293sp22-project0
Text Analytics - Project 0 

Execute Command: pipenv run python project0/main.py --incidents <url>

Main.py
=======
=> Main program function that imports Project0.py functions to execute and complete the various tasks as per the requirments found at below url:

https://oudatalab.com/cs5293sp22/projects/project0

=> project0 package is imported.

=>User provides url of the pdf file for the particular incident report to be analyzed

=> Fetch_data(url) executes and returns pdf

=> extract_data(data) extractes, segregates and writes all the data in a csv file

=> create_db(db_name) creates a new db and creates the table incidents

=> Insert_data(db_name) extracts values from the csv file and writes it into the table incidents

=> status(db_name) returns data which contains the type of incident nature and the number of times it occuered.

=> The returened data is now displayed in required format.

Project0 Funtions
=================
**1. fetch_data(url)**

=> The url provided by the user is user in command line argument to retrive incident data in pdf format. It returns data in pdf format


**2. extract_data(data)**

=> The data retrieved from fetch_data(url) is passed as argument.

=> A Csv file is opened to write down the extracted data into csv format for further use.

=> Loops through each page of the pdf one by one.

=> It converts the pdf data as recieved in argument into readable text format using the PyPDF2 library.

=> In some cases, address have 2 lines. Using regular expressions the address is merged into a singular line for simplicity.

=> Initial page of the pdf contains column headers, they are converted into the column names that will be used for table in sqlite3 database for easier insertion operation

=> All data is split on the newline('\n') to seperate all the data.

=> Initialized a counter and row to store each row data

=> Loop through each value in the current page

=> With the help of a counter which increments from 0 to 4, created each row of data of 5 values.

=> In case Addressm and Nature is missing, used regex to check if the 3rd column value is same as what is suppossed to be in the 5th column and added data values "No data" for the specific case as while the library complete ignores empty fields in the pdf.

=> Each row is then writtern into the open csv file and a list that contains all the rows of data.

=> Counter and row value is re-initialized to 0 and null respectively for the next 5 sets of data.

=> Loop contines till all data is sorted into array of size 5.


**3. create_db(db_name)**

=> Checks in the current folder if a database while the value specified in argument exists or not. If yes, it removes it.

=> Creates new database with argument db_name

=> Create the incident table into the newly created database


**4. insert_data(db_name)**

=> Opens the csv file where all the extracted data from the pdf is stored

=> Connects to database <db_name>

=> Inserts the data into the table incidents in database <db_name> via insert statement 


**5. status(db_name)** 

=> Connects to database <db_name>

=> Executes select statment to find out the type of nature of the incident and the number of time it occured.

=> Returns the result to the main function for display


TEST CASES
==========

Set Test url to be used as:

url='https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-21_daily_incident_summary.pdf'                    

**1.test_fetch_data(test_url)**

=> Fetch_data(url) returns pdf data. The length of the pdf data should be 374028 as checked manually.


**2.test_extract_data(test_url)**

=> Used fetch_data(url) to retrive data. 

=> It is passed as the argument for extract_data(data). The function should create a csv file called Extraced_data.csv where all the data is extracted and segregated.

=> It checks in the current directory if the csv file exists or not and if the size of the file is equal to 318 (header row + 317 rows of data)

=> If the condition satsifies then it pasts the test


**3.test_create_table()**

=> Execute function create_table(db_name) to create database normanpd.db and table incidents

=> It checks if in the current directory the normanpd.db file exists or not. Test passes if the database is found.

**4.test_insert_table()**

=> Executes function insert_table(db_name) to insert data from the csv file created before into table incidents

=> Execute select statment to find count of total rows inside the table to check if insertion worked or not.

=> If the number of rows is equal to 317 then the test passes and all rows are inserted.

**5.test_status(db_name)**

=> Executes function status(db_name) to execute select statment to find different nature of incidents and the no of times it occurred. 

=> It compares with the length of the result set returned which should be 64 as there are 64 unique nature values.

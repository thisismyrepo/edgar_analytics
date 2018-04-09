Input: existing publicly available EDGAR weblogs. Assume that each line represents a single web request for an EDGAR document that would be streamed into your program in real time.
Using the data, identify when a user visits, calculate the duration of and number of documents requested during that visit, and then write the output to a file.
2 input files: 
•	log.csv: EDGAR weblog data
•	inactivity_period.txt: Holds a single value denoting the period of inactivity (in seconds) that should be used to identify when a user session is over
1 output file:
•	sessionization.txt, listing the IP address, duration of the session and number of documents 
The fields on each line must be separated by a ,:
•	IP address of the user exactly as found in log.csv
•	date and time of the first webpage request in the session (yyyy-mm-dd hh:mm:ss)
•	date and time of the last webpage request in the session (yyyy-mm-dd hh:mm:ss)
•	duration of the session in seconds
•	count of webpage requests during the session



Relevant data fields:
•	ip: identifies the IP address of the device requesting the data. While the SEC anonymizes the last three digits, it uses a consistent formula that allows you to assume that any two ip fields with the duplicate values are referring to the same IP address
•	date: date of the request (yyyy-mm-dd)
•	time: time of the request (hh:mm:ss)
•	cik: SEC Central Index Key
•	accession: SEC document accession number
•	extention: Value that helps determine the document being requested
you can assume the combination of cik, accession and extention fields uniquely identifies a single web page document request. Don't assume any particular format for any of those three fields (e.g., the fields can consist of numbers, letters, hyphens, periods and other characters)

The first line of log.csv will be a header denoting the names of the fields in each web request. Each field is separated by a comma. Your program should only use this header to determine the order in which the fields will appear in the rest of the other lines in the same file.
inactivity_period.txt
This file will hold a single integer value denoting the period of inactivity (in seconds) that your program should use to identify a user session. The value will range from 1 to 86,400 (i.e., one second to 24 hours)


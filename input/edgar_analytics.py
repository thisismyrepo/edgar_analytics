# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:59:26 2018

@author: Thinkpad
"""

# import math
# import re
import pandas as pd
# import numpy as np



#input_file = "/input/log.csv"
#fileHandle = open('input_file', 'r')       # Opening input file "log.csv"

fileHandle = """
ip,date,time,zone,cik,accession,extention,code,size,idx,norefer,noagent,find,crawler,browser
101.81.133.jja,2017-06-30,00:00:00,0.0,1608552.0,0001047469-17-004337,-index.htm,200.0,80251.0,1.0,0.0,0.0,9.0,0.0,
107.23.85.jfd,2017-06-30,00:00:00,0.0,1027281.0,0000898430-02-001167,-index.htm,200.0,2825.0,1.0,0.0,0.0,10.0,0.0,
107.23.85.jfd,2017-06-30,00:00:00,0.0,1136894.0,0000905148-07-003827,-index.htm,200.0,3021.0,1.0,0.0,0.0,10.0,0.0,
107.23.85.jfd,2017-06-30,00:00:01,0.0,841535.0,0000841535-98-000002,-index.html,200.0,2699.0,1.0,0.0,0.0,10.0,0.0,
108.91.91.hbc,2017-06-30,00:00:01,0.0,1295391.0,0001209784-17-000052,.txt,200.0,19884.0,0.0,0.0,0.0,10.0,0.0,
106.120.173.jie,2017-06-30,00:00:02,0.0,1470683.0,0001144204-14-046448,v385454_20fa.htm,301.0,663.0,0.0,0.0,0.0,10.0,0.0,
107.178.195.aag,2017-06-30,00:00:02,0.0,1068124.0,0000350001-15-000854,-xbrl.zip,404.0,784.0,0.0,0.0,0.0,10.0,1.0,
107.23.85.jfd,2017-06-30,00:00:03,0.0,842814.0,0000842814-98-000001,-index.html,200.0,2690.0,1.0,0.0,0.0,10.0,0.0,
107.178.195.aag,2017-06-30,00:00:04,0.0,1068124.0,0000350001-15-000731,-xbrl.zip,404.0,784.0,0.0,0.0,0.0,10.0,1.0,
108.91.91.hbc,2017-06-30,00:00:04,0.0,1618174.0,0001140361-17-026711,.txt,301.0,674.0,0.0,0.0,0.0,10.0,0.0,
"""

#input_file2 = "/input/inactivity_period.txt"     # inactivity period in seconds, read this value from "inactivity_period.txt"
#inactivity_period = open('input_file2','r')
#for line in fileHandle:
#    fields = line.split(',')
#    
#
#
## input_data = re.sub(r'( )', r',\1', fileHandle)   
#input_data = re.sub("\s+", ",",fileHandle)
#fields = input_data.split(',')                       # Splits data into separate indices
#del fields[0]
#counter = 0
#
#
data = pd.read_csv('log.csv')

NumberOfRowsInData = data.shape[0]
NumberOfCols = 15
#
#
#df = pd.DataFrame(fields)

# output file: sessionization.txt. The fields on each line must be separated by a ,:
#
# IP address of the user exactly as found in log.csv
# date and time of the first webpage request in the session (yyyy-mm-dd hh:mm:ss)
# date and time of the last webpage request in the session (yyyy-mm-dd hh:mm:ss)
# duration of the session in seconds
# count of webpage requests during the session

# Group data by IP, then get the first and last date and time for each IP. 



# newdata = list(data.groupby('ip', as_index=False))

time = data.groupby('ip').time.agg(['min','max'])
date = data.groupby('ip').date.agg(['min','max'])
IP_addresses = time.index
NumberOfRowsInTime = time.shape[0]
value=0
i=0
CountOfRequests = 0
outputfile = open('/output/sessionization.txt','a') 

while value <= NumberOfRowsInTime:
    UserIP = IP_addresses[value]
    FirstTime = time.loc[IP_addresses[value], "min"]
    LastTime = time.loc[IP_addresses[value], "max"] 
#    SessionDuration = LastTime - FirstTime
    FirstDate = date.loc[IP_addresses[value], "min"]
    LastDate = date.loc[IP_addresses[value], "max"] 
#    while i <= NumberOfRowsInData:                       # Counting number of requests. This causes the code to be very slow for some reason.
#        if data.loc[i,"ip"]==UserIP:
#            CountOfRequests = CountOfRequests + 1
#            i=i+1
    print(UserIP,',',FirstDate,FirstTime,',',LastDate,LastTime,',')
    outputfile.write(UserIP,',',FirstDate,FirstTime,',',LastDate,LastTime)
    value=value+1
    CountOfRequests=0
    i=0

#def calculate_duration(row):
#        return row['max']-row['min']
#    
#time['duration']=time.apply(calculate_duration, axis=1)

#time['duration']=time['max']-time['min']

#for i in range(time.shape[0]):  # iterate over rows
#    duration[i] = max[i] - min[i]
    

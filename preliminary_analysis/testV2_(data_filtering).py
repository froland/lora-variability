import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

##############################################################################################
#This part will filter the .csv file (remove duplicates, elements before activation date, ...)
##############################################################################################

data=pd.read_csv('loravar.csv', sep=',') #Reading the .csv file
data=data.drop_duplicates() #Dropping the duplicates

deletion_list = [] #Creating a deletion list to append indices of lines to remove
for index, row in data.iterrows():
    if(row['dev_id']=='mobile-03'): #Dropping mobile-03 node as it was not active in this case
        deletion_list.append(index) #Appending indices of lines to remove
        
data=data.drop(labels = deletion_list, axis = 0) #Axis = 0 means we remove rows/lines (not columns)
data=data.reset_index(drop=True) #Resetting the indices after dropping (drop=True puts the new indices in place of old ones)

data['received'] =  pd.to_datetime(data['received']) #Converting strings to datetime format (supported by Python)
#Datetime of activation of each device
date_602 = datetime.strptime('2019-04-04T12:50:0.0Z', '%Y-%m-%dT%H:%M:%S.%fZ') #year-month-day hour-minute-seconds-fraction_of_seconds
date_603 = datetime.strptime('2019-04-04T12:25:0.0Z', '%Y-%m-%dT%H:%M:%S.%fZ')
date_701 = datetime.strptime('2019-04-05T17:30:0.0Z', '%Y-%m-%dT%H:%M:%S.%fZ')
date_601 = datetime.strptime('2019-04-25T22:45:0.0Z', '%Y-%m-%dT%H:%M:%S.%fZ')
date_702 = datetime.strptime('2019-04-05T13:15:0.0Z', '%Y-%m-%dT%H:%M:%S.%fZ')
date_801 = datetime.strptime('2019-04-05T14:45:0.0Z', '%Y-%m-%dT%H:%M:%S.%fZ')

#Removing data send by devices before they were setup
deletion_list = []
for index, row in data.iterrows():
    if(row['received'] < date_602 and row['dev_id'] == 'static_6_02'):
        deletion_list.append(index)
    if(row['received'] < date_603 and row['dev_id'] == 'static_6_03'):
        deletion_list.append(index)
    if(row['received'] < date_701 and row['dev_id'] == 'static_7_01'):
        deletion_list.append(index)
    if(row['received'] < date_601 and row['dev_id'] == 'static_6_01'):
        deletion_list.append(index)
    if(row['received'] < date_702 and row['dev_id'] == 'static_7_02'):
        deletion_list.append(index)
    if(row['received'] < date_801 and row['dev_id'] == 'static_8_01'):
        deletion_list.append(index)

data=data.drop(labels = deletion_list, axis = 0)
data=data.reset_index(drop=True)
data.to_csv('filtered_loravar.csv', sep=',', index=False)

#Add lines to remove packets from the Third gateway (no timestamp given)
deletion_list = []
for index, row in data.iterrows():
    if(row['gtw_id'] == 'rg1xx294c6e'):
        deletion_list.append(index)

data=data.drop(labels = deletion_list, axis = 0)
data=data.reset_index(drop=True)
data.to_csv('filtered_3rdgtw_loravar.csv', sep=',', index=False)

results = data.shape
results = results[0] #Total number of samples we have collected

'''

########################################################
#This part will focus on the scatter plot of the results
########################################################

#Taking points only from one gateway (Houzeau gateway (eui-0000024b08030186) or iotlab-rpi-03 or rg1xx294c6e)
gtwdf = data.copy()

gtw_id = 'iotlab-rpi-03'
deletion_list = []
for index, row in gtwdf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)
        
gtwdf=gtwdf.drop(labels = deletion_list, axis = 0)
gtwdf=gtwdf.reset_index(drop=True)

unique_list_gtw = []
for element in gtwdf.dev_id:
    if(element not in unique_list_gtw):
        unique_list_gtw.append(element) #Show which and how many device(s) have sent packets to this gateway



toscatterplot = gtwdf.copy()
deletion_list=[]
dev_id = 'static_7_01'
for index, row in gtwdf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
'''

'''   
#Taking points only from one device
devicedf = data.copy()

dev_id = 'static_8_01'
deletion_list = []
for index, row in devicedf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)
        
devicedf=devicedf.drop(labels = deletion_list, axis = 0)
devicedf=devicedf.reset_index(drop=True)

unique_list_dev = []
for element in devicedf.gtw_id:
    if(element not in unique_list_dev):
        unique_list_dev.append(element) #Show which and how many gateway(s) have receieved packets from the device
'''

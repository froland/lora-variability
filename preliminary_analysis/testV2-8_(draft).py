import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from haversine import haversine
import re

data=pd.read_csv('loravar_distances_copy.csv', sep=',')
data['received'] =  pd.to_datetime(data['received'])
results = data.shape
results = results[0]
'''

ax1 = data.plot(x='frequency', y='rssi',  style = '.', title = 'RSSI for each carrier frequency', grid=True, fontsize = 14)
ax1.legend([])
ax1.set_xlabel("Carrier frequency (MHz)", fontsize = 14)            
ax1.set_ylabel("RSSI (dBm)", fontsize = 14)
ax1.title.set_size(14)


#ax0=data.data_rate.hist()

date_init = datetime.strptime('2019-04-05T00:00:0.0Z', '%Y-%m-%dT%H:%M:%S.%fZ')
date_fin = datetime.strptime('2019-04-08T00:00:0.0Z', '%Y-%m-%dT%H:%M:%S.%fZ')
deletion_list = []
for index, row in data.iterrows():
    if(row['received'] < date_init or row['received'] > date_fin):
        deletion_list.append(index)
data=data.drop(labels = deletion_list, axis = 0)
data=data.reset_index(drop=True)


dev_id = 'static_7_02'
deletion_list = []
for index, row in data.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)
data=data.drop(labels = deletion_list, axis = 0)
data=data.reset_index(drop=True)

gtw_id = 'eui-0000024b08030186'
#gtw_id = 'iotlab-rpi-03'
deletion_list = []
for index, row in data.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)
data=data.drop(labels = deletion_list, axis = 0)
data=data.reset_index(drop=True)


ax1 = data.plot(x='received', y='pressure',  style = '.', title = 'Case : 7_02 to eui-0000024b08030186', grid=True, fontsize = 11)
ax1.legend([])
ax1.set_xlabel("Time", fontsize = 12)
ax1.set_ylabel("Pressure (Pa)", fontsize = 12)
ax1.title.set_size(14)

#ax1 = data.boxplot(column=['snr'])
#ax1.legend([dev_id, gtw_id])
#ax1.set_xlabel("RSSI (dBm)")            
#ax1.set_ylabel("SNR (dB)") 

'''
ax1 = data.plot(x='humidity', y='snr',  style = 'o', title = 'title', grid=True, fontsize = 14)
ax1.legend([])
ax1.set_xlabel("x", fontsize = 14)            
ax1.set_ylabel("y", fontsize = 14)
ax1.title.set_size(14)
'''
#iotlab-rpi-03
#eui-0000024b08030186
'''
#data = data [['data_rate','rssi','snr','humidity','pressure','temperature', 'dist_devgtw']]
#pdpearson = data.corr(method ='pearson')
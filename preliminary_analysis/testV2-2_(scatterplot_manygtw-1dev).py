import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

data=pd.read_csv('filtered_loravar.csv', sep=',')
data['received'] =  pd.to_datetime(data['received'])
results = data.shape
results = results[0]

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

toscatterplot = devicedf.copy()
deletion_list=[]
gtw_id = 'eui-0000024b08030186'
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)
    
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax1 = toscatterplot.plot.scatter(x='snr', y='rssi', c='#0000FF', title = 'Packets sent by static_8_01', grid=True)
ax1.legend(['eui-0000024b08030186'])
ax1.set_xlabel("SNR (dB)")            
ax1.set_ylabel("RSSI (dBm)")        

'''
toscatterplot = devicedf.copy()
deletion_list=[]
gtw_id = 'eui-0000024b08030186'
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax1 = toscatterplot.plot.scatter(x='pressure', y='rssi', c='#0000FF')

toscatterplot = devicedf.copy()
deletion_list=[]
gtw_id = 'iotlab-rpi-03'
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)
    
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax2 = toscatterplot.plot.scatter(x='pressure', y='rssi', c='#FF0000', title = 'Packets sent by static_7_02', grid=True, ax=ax1)
ax2.legend(['eui-0000024b08030186', 'iotlab-rpi-03'])
ax2.set_xlabel("Pressure (Pa)")            
ax2.set_ylabel("RSSI (dBm)")        
'''        
###########################################################################     
'''      
toscatterplot = devicedf.copy()
deletion_list=[]
gtw_id = 'eui-0000024b08030186'
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax1 = toscatterplot.plot.scatter(x='snr', y='rssi', c='#0000FF')

toscatterplot = devicedf.copy()
deletion_list=[]
gtw_id = 'iotlab-rpi-03'
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)
    
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax2 = toscatterplot.plot.scatter(x='snr', y='rssi', c='#FF0000', title = 'Packets sent by static_7_01', grid=True, ax=ax1)
ax2.legend(['eui-0000024b08030186', 'iotlab-rpi-03'])
ax2.set_xlabel("SNR (dB)")            
ax2.set_ylabel("RSSI (dBm)")
'''       
##############################################################################
'''
toscatterplot = devicedf.copy()
deletion_list=[]
gtw_id = 'eui-0000024b08030186'
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax1 = toscatterplot.plot.scatter(x='humidity', y='rssi', c='#0000FF')

toscatterplot = devicedf.copy()
deletion_list=[]
gtw_id = 'iotlab-rpi-03'
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)
    
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax2 = toscatterplot.plot.scatter(x='humidity', y='rssi', c='#FF0000', title = 'Packets sent by static_6_03', grid=True, ax=ax1)
ax2.legend(unique_list_dev)
ax2.set_xlabel("Relative humidity (%)")            
ax2.set_ylabel("RSSI (dBm)")
'''

##############################################################################
'''
toscatterplot = devicedf.copy()
deletion_list=[]
gtw_id = 'eui-0000024b08030186'
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)
    
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax1 = toscatterplot.plot.scatter(x='humidity', y='rssi', c='#0000FF', title = 'Packets sent by static_6_02', grid=True)
ax1.legend(unique_list_dev)
ax1.set_xlabel("Relative humidity (%)")            
ax1.set_ylabel("RSSI (dBm)")
'''
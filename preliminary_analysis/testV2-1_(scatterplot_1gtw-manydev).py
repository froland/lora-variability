import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

data=pd.read_csv('filtered_loravar.csv', sep=',')
data['received'] =  pd.to_datetime(data['received'])
results = data.shape
results = results[0]

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

#Checking which devices have communicated with this gateway
unique_list_gtw = []
for element in gtwdf.dev_id:
    if(element not in unique_list_gtw):
        unique_list_gtw.append(element)
'''
toscatterplot = gtwdf.copy()
deletion_list=[]
dev_id = 'static_6_01'
for index, row in gtwdf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)


toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax1 = toscatterplot.plot.scatter(x='snr', y='rssi', c='#00FF00')
                                 
                                                               
toscatterplot = gtwdf.copy()
deletion_list=[]
dev_id = 'static_7_01'
for index, row in gtwdf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax2 = toscatterplot.plot.scatter(x='snr', y='rssi', c='#FF4500', ax=ax1)  
                                 
                                 
                                 
toscatterplot = gtwdf.copy()
deletion_list=[]
dev_id = 'static_8_01'
for index, row in gtwdf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax3 = toscatterplot.plot.scatter(x='snr', y='rssi', c='#800000', title = 'Packets received at the gateway rg1xx294c6e', grid=True, ax=ax2)     
ax3.legend(unique_list_gtw)
ax3.set_xlabel("SNR (dB)")            
ax3.set_ylabel("RSSI (dBm)")     
'''

                           

'''    
toscatterplot = gtwdf.copy()
deletion_list=[]
dev_id = 'static_6_03'
for index, row in gtwdf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax1 = toscatterplot.plot(x='received', y='pressure', c='#00BFFF', style = 'o')

                                 
toscatterplot = gtwdf.copy()
deletion_list=[]
dev_id = 'static_6_02'
for index, row in gtwdf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax2 = toscatterplot.plot(x='received', y='pressure', c='#006400', style = 'o', ax=ax1)                                 


toscatterplot = gtwdf.copy()
deletion_list=[]
dev_id = 'static_7_02'
for index, row in gtwdf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax3 = toscatterplot.plot(x='received', y='pressure', c='#FF8C00', style = '.', ax=ax2)


toscatterplot = gtwdf.copy()
deletion_list=[]
dev_id = 'static_8_01'
for index, row in gtwdf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax4 = toscatterplot.plot(x='received', y='pressure', c='#FF0000', style = '.', ax=ax3)



toscatterplot = gtwdf.copy()
deletion_list=[]
dev_id = 'static_7_01'
for index, row in gtwdf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax5 = toscatterplot.plot(x='received', y='pressure', c='#00FF00', style = '.', title = 'Packets received at the gateway eui-0000024b08030186', grid=True, ax=ax4)
ax5.legend(unique_list_gtw)
ax5.set_xlabel("Time")            
ax5.set_ylabel("Pressure (Pa)")    
'''

##############################################################################
                                               

toscatterplot = gtwdf.copy()
deletion_list=[]
dev_id = 'static_6_03'
for index, row in gtwdf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax1 = toscatterplot.plot(x='received', y='pressure', c='#00BFFF', style = 'o')

                                 
toscatterplot = gtwdf.copy()
deletion_list=[]
dev_id = 'static_7_01'
for index, row in gtwdf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax2 = toscatterplot.plot(x='received', y='pressure', c='#006400', style = '.', ax=ax1)


toscatterplot = gtwdf.copy()
deletion_list=[]
dev_id = 'static_7_02'
for index, row in gtwdf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)

toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax3 = toscatterplot.plot(x='received', y='pressure', c='#FF8C00', style = 'o', ax=ax2, title = 'Packets received at the gateway iotlab-rpi-03', grid=True)
ax3.legend(unique_list_gtw)
ax3.set_xlabel("Time")            
ax3.set_ylabel("Pressure (Pa)")    
    
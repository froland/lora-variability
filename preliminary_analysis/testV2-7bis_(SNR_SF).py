import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

data_sf=pd.read_csv('loravar_distances_copy.csv', sep=',')
data_sf['received'] =  pd.to_datetime(data_sf['received'])
results = data_sf.shape
results = results[0]

#pdpearson=data_sf.corr(method='pearson')

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y'], str(point['val']))


devicedf = data_sf.copy()

dev_id = 'static_7_02'
deletion_list = []
for index, row in devicedf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)      
devicedf=devicedf.drop(labels = deletion_list, axis = 0)
devicedf=devicedf.reset_index(drop=True)

gtw_id = 'eui-0000024b08030186'
deletion_list=[]
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)
devicedf=devicedf.drop(labels = deletion_list, axis = 0)
devicedf=devicedf.reset_index(drop=True)

unique_list_sf = []
for element in devicedf.data_rate:
    if(element not in unique_list_sf):
        unique_list_sf.append(element)

toscatterplot = devicedf.copy()
deletion_list=[]
sf = 7
for index, row in devicedf.iterrows():
    if(row['data_rate'] != sf):
        deletion_list.append(index)
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax1 = toscatterplot.plot(x='snr', y='rssi', c='#000000', style = 'o')
#label_point(toscatterplot.received, toscatterplot.rssi, toscatterplot.data_rate, ax1)

toscatterplot = devicedf.copy()
deletion_list=[]
sf = 8
for index, row in devicedf.iterrows():
    if(row['data_rate'] != sf):
        deletion_list.append(index)
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax2 = toscatterplot.plot(x='snr', y='rssi', c='#FF0000', style = 'o', ax=ax1)
#label_point(toscatterplot.received, toscatterplot.rssi, toscatterplot.data_rate, ax1)

toscatterplot = devicedf.copy()
deletion_list=[]
sf = 9
for index, row in devicedf.iterrows():
    if(row['data_rate'] != sf):
        deletion_list.append(index)
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax3 = toscatterplot.plot(x='snr', y='rssi', c='#0000FF', style = 'o', ax=ax2)
#label_point(toscatterplot.received, toscatterplot.rssi, toscatterplot.data_rate, ax1)

toscatterplot = devicedf.copy()
deletion_list=[]
sf = 10
for index, row in devicedf.iterrows():
    if(row['data_rate'] != sf):
        deletion_list.append(index)
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax4 = toscatterplot.plot(x='snr', y='rssi', c='#008000', style = 'o', ax=ax3)
#label_point(toscatterplot.received, toscatterplot.rssi, toscatterplot.data_rate, ax1)
                         
toscatterplot = devicedf.copy()
deletion_list=[]
sf = 11
for index, row in devicedf.iterrows():
    if(row['data_rate'] != sf):
        deletion_list.append(index)
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax5 = toscatterplot.plot(x='snr', y='rssi', c='#1E90FF', style = 'o',ax=ax4)
#label_point(toscatterplot.received, toscatterplot.rssi, toscatterplot.data_rate, ax2)

toscatterplot = devicedf.copy()
deletion_list=[]
sf = 12
for index, row in devicedf.iterrows():
    if(row['data_rate'] != sf):
        deletion_list.append(index)
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax6 = toscatterplot.plot(x='snr', y='rssi', c='#FF4500', style = 'o', title = 'Packets sent by static_7_02 and received by eui-0000024b08030186', grid=True, ax=ax5, fontsize = 14)
ax6.legend(['SF7','SF8','SF9', 'SF10', 'SF11', 'SF12'], fontsize = 14)
ax6.set_xlabel("SNR (dB)", fontsize = 14)            
ax6.set_ylabel("RSSI (dBm)", fontsize = 14)
ax6.title.set_size(14)
#label_point(toscatterplot.received, toscatterplot.rssi, toscatterplot.data_rate, ax3)

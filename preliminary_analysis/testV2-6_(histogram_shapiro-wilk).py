import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy import stats
from scipy.stats import shapiro

data=pd.read_csv('filtered_3rdgtw_loravar.csv', sep=',')
data['received'] =  pd.to_datetime(data['received'])
results = data.shape
results = results[0]

devicedf = data.copy()

dev_id = 'static_7_02'
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

histogramplot = devicedf.copy()
deletion_list=[]
gtw_id = unique_list_dev[0]
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)
        
histogramplot=histogramplot.drop(labels = deletion_list, axis = 0)
histogramplot=histogramplot.reset_index(drop=True)


W,p = shapiro(histogramplot.rssi-histogramplot.rssi.mean())
#A2, critical, sig = anderson(histogramplot.snr, dist='norm')
#ax0 = histogramplot.rssi.hist()
#ax1 = histogramplot.snr.hist()
#ax2 = histogramplot.temperature.hist()
#ax3 = histogramplot.humidity.hist()
#ax4 = histogramplot.pressure.hist()
#ax1 = histogramplot.boxplot(column=['snr'])
#stats.probplot(histogramplot.humidity, plot=plt)

'''
An article recommends that both visual and normality tests should be used to assess that data follows a normal distribution.
Besides, checking that data is normally distributed allows to use parametric tests (which are the most used ones in practice).
Apparently, Pearson is a paramteric test.
Kolmogorov-Smirnov test is considerd obsolete when compared to Shapiro-Wilk.
'''
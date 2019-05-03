import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

data=pd.read_csv('filtered_3rdgtw_loravar.csv', sep=',')
data['received'] =  pd.to_datetime(data['received'])
results = data.shape
results = results[0]

devicedf = data.copy()

dev_id = 'static_8_01'
deletion_list = []
for index, row in devicedf.iterrows():
    if(row['dev_id'] != dev_id):
        deletion_list.append(index)
        
devicedf=devicedf.drop(labels = deletion_list, axis = 0)
devicedf=devicedf.reset_index(drop=True)

ax1 = devicedf.boxplot(column=['snr'])
ax1.legend([dev_id])
#ax1.set_xlabel("RSSI (dBm)")            
ax1.set_ylabel("SNR (dB)") 
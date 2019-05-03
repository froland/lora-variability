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

unique_list_dev = []
for element in devicedf.gtw_id:
    if(element not in unique_list_dev):
        unique_list_dev.append(element)

deletion_list=[]
gtw_id = unique_list_dev[0]
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)

devicedf=devicedf.drop(labels = deletion_list, axis = 0)
devicedf=devicedf.reset_index(drop=True)

pdpearson=devicedf.corr(method='pearson')

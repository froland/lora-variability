import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('loravar_deltas.csv', sep=',')
data['received'] =  pd.to_datetime(data['received'])
results = data.shape
results = results[0]
'''
variations = []
for i, r in data.iterrows():
    if(i+1 == results):
        break
    t1 = data.loc[i]['rssi']
    t2 = data.loc[i+1]['rssi']
    delta = t2-t1
    variations.append(delta)

deltadf = pd.DataFrame(variations, columns = ['delta_rssi'])
data = data.join(deltadf)

variations = []
for i, r in data.iterrows():
    if(i+1 == results):
        break
    t1 = data.loc[i]['snr']
    t2 = data.loc[i+1]['snr']
    delta = t2-t1
    variations.append(delta)

deltadf = pd.DataFrame(variations, columns = ['delta_snr'])
data = data.join(deltadf)


variations = []
for i, r in data.iterrows():
    if(i+1 == results):
        break
    t1 = data.loc[i]['temperature']
    t2 = data.loc[i+1]['temperature']
    delta = t2-t1
    variations.append(delta)

deltadf = pd.DataFrame(variations, columns = ['delta_temp'])
data = data.join(deltadf)

variations = []
for i, r in data.iterrows():
    if(i+1 == results):
        break
    t1 = data.loc[i]['humidity']
    t2 = data.loc[i+1]['humidity']
    delta = t2-t1
    variations.append(delta)

deltadf = pd.DataFrame(variations, columns = ['delta_humid'])
data = data.join(deltadf)

variations = []
for i, r in data.iterrows():
    if(i+1 == results):
        break
    t1 = data.loc[i]['pressure']
    t2 = data.loc[i+1]['pressure']
    delta = t2-t1
    variations.append(delta)

deltadf = pd.DataFrame(variations, columns = ['delta_press'])
data = data.join(deltadf)
'''
pdpearson = data.corr(method = 'pearson')
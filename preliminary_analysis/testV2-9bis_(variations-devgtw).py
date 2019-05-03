import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

data=pd.read_csv('loravar_distances_copy.csv', sep=',')
data['received'] =  pd.to_datetime(data['received'])
results = data.shape
results = results[0]

#globalpearson = data.corr(method = 'pearson')


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

#localpearson = data.corr(method = 'pearson')

'''
z = np.polyfit(x=data.index.values, y=data.rssi, deg=1)
p = np.poly1d(z)
'''


results = data.shape
results = results[0]

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

localpearson = data.corr(method = 'pearson')


'''
ax1 = data.plot(x='delta_temp', y='rssi', c='#000000', style = 'o')
#ax1.legend(['SF7','SF8','SF9', 'SF10', 'SF11', 'SF12'], fontsize = 14)
ax1.set_xlabel("x", fontsize = 14)            
ax1.set_ylabel("y", fontsize = 14)
ax1.title.set_size(14)
'''

'''
IMPORTANT !!! Si on regarde les variations de températures/pression/humidité, il faut calculer ces variations sur le dataframe nettoyé.
C'est-à-dire qu'il faut d'abord selectionner le cas qui nous interesse et ensuite on peut calculer les variations.
Si on calcule d'abord les variations puis que l'on nettoie, on a des erreurs.
'''
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 11:15:56 2019

@author: Nikola
"""

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

df=pd.read_csv('loradummytrain.csv', sep=';')

#print(type(df['snr'][0]))

example = df.loc[:, "rssi":"rain_quan"]

x = df.loc[:, "temp_30"]
y = df.loc[:, "rssi"]

plt.scatter(x, y)

pearson = np.corrcoef(x,y, rowvar = False)
covmatx = np.cov(x, y, rowvar = False)


pearson2 = np.corrcoef(example, rowvar = False)
covmatx2 = np.cov(example, rowvar = False)

pearson3 = np.corrcoef(df, rowvar = False)

#----------

from haversine import haversine

devloc=pd.read_csv('dummydevlocation.csv', sep=',')
gtwloc=pd.read_csv('dummygtwlocation.csv', sep=',')

devloc = devloc.values
gtwloc = gtwloc.values

loc1 = (devloc[1,1], devloc[1,2])
loc2 = (gtwloc[1,1], gtwloc[1,2]) #Could put these lines in a loop

hav = haversine(loc1, loc2) #distance in kilometers
hav=hav*1000 #distance in meters
distance = (hav**2 + (devloc[0,3]-gtwloc[0,3])**2)**(0.5) #in meters

#----------

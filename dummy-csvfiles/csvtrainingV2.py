################################
#Library call and histogram plot
################################

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from haversine import haversine

pkgw=pd.read_csv('pk-gw-dummy.csv', sep=';')
weather=pd.read_csv('weather.csv', sep=';')

pkgw = pkgw.sort_values(by = 'timestmp')

#plt.hist(weather.temp_3m)

#rssi = pkgw[["rssi"]]
#rssi = rssi.values
#pkgw.rssi = pkgw.rssi /10
#pkgw.rssi = np.float_power(10, pkgw.rssi)
plt.hist(pkgw.rssi) #Example of histogram plot with RSSI values

###################################################################
#Calculating distance between gw and dev and adding it to dataframe
###################################################################

gwloc=pd.read_csv('gateway_location.csv', sep=';')

tableofdistance = []
indices = []
for index, row in pkgw.iterrows():
        for index_gw, row_gw in gwloc.iterrows():
            if (row['gw_id'] == row_gw['gw_id']):
                loc1 = (pkgw.loc[index]['dev_lat'], pkgw.loc[index]['dev_long'])
                loc2 = (gwloc.loc[index_gw]['gw_lat'], gwloc.loc[index_gw]['gw_long'])
                hav = haversine(loc1, loc2)
                hav=hav*1000 #Distance in meters (By default, haversine returns in kilometers)
                distance = (hav**2 + (pkgw.loc[index]['dev_alt']-gwloc.loc[index_gw]['gw_alt'])**2)**(0.5)
                tableofdistance.append(distance)
                indices.append(index)
                
distanceDF = pd.DataFrame(tableofdistance, columns = ['distance_dev-gw'], index = indices)
pkgw = pkgw.join(distanceDF) #The distance between each gateway and device is added to the main data frame

########################
#Scatter plot of my data
########################

#pkgw.rssi = pkgw.rssi /10
#pkgw.rssi = np.float_power(10, pkgw.rssi) #to pass rssi from dBm to mW
ax1 = pkgw.plot.scatter(x='rssi', y='distance_dev-gw')
ax2 = pkgw.plot.scatter(x='snr', y='rssi')

bigdata = pd.concat([pkgw, weather], axis = 1,ignore_index = False)

ax3 = bigdata.plot.scatter(x='temp_30m', y ='rssi')
bigdata.temp_30m = np.log10(bigdata.temp_30m)
ax4 = bigdata.plot.scatter(x='temp_30m', y ='rssi')

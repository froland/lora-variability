import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from haversine import haversine

data=pd.read_csv('filtered_3rdgtw_loravar.csv', sep=',')
data['received'] =  pd.to_datetime(data['received'])
results = data.shape
results = results[0]

devloc=pd.read_csv('device_location.csv', sep=';')
gtwloc=pd.read_csv('gateway_location.csv', sep=';')


tableofdistance = []
indices = []
for index, row in data.iterrows():
        for index_gtw, row_gtw in gtwloc.iterrows():
            for index_dev, row_dev in devloc.iterrows():
                if(row['gtw_id'] == row_gtw['gtw_id'] and row['dev_id'] == row_dev['dev_id']):
                    loc1 = (devloc.loc[index_dev]['dev_lat'], devloc.loc[index_dev]['dev_long'])
                    loc2 = (gtwloc.loc[index_gtw]['gtw_lat'], gtwloc.loc[index_gtw]['gtw_long'])
                    hav = haversine(loc1, loc2)
                    hav=hav*1000 #Distance in meters (By default, haversine returns in kilometers)
                    distance = (hav**2 + (devloc.loc[index_dev]['dev_alt']-gtwloc.loc[index_gtw]['gtw_alt'])**2)**(0.5)
                    tableofdistance.append(distance)
                    
distanceDF = pd.DataFrame(tableofdistance, columns = ['dist_devgtw'])
data_distance = data.join(distanceDF)

data_distance.to_csv('loravar_distances.csv', sep=',', index=False)
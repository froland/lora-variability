import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.linear_model import LinearRegression

data=pd.read_csv('filtered_3rdgtw_loravar.csv', sep=',')
data['received'] =  pd.to_datetime(data['received'])
results = data.shape
results = results[0]

#Taking points only from one device
devicedf = data.copy()

dev_id = 'static_6_03'
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

toscatterplot = devicedf.copy()
deletion_list=[]
gtw_id = unique_list_dev[0]
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)
        
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax1 = toscatterplot.plot(x='received', y='rssi', c='#0000FF', style = '.',  title = 'Packets sent by static_8_01', grid=True)
ax1.legend([unique_list_dev[0]])
ax1.set_xlabel("Time")            
ax1.set_ylabel("Relative humidity (%)")

X = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
Y = data.iloc[:, 8].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X) # make predictions


'''
lin_regression = LinearRegression()
lin_regression.fit(toscatterplot.received,toscatterplot.rssi)
m = lin_regression.coef_
b = lin_regression.intercept_
predictions = lin_regression.predict(toscatterplot.received)
print ("formula: y = {0}x + {1}".format(m, b))
'''

'''
toscatterplot = devicedf.copy()
deletion_list=[]
gtw_id = unique_list_dev[0]
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)
        
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax1 = toscatterplot.plot(x='received', y='humidity', c='#0000FF', style = 'o')

toscatterplot = devicedf.copy()
deletion_list=[]
gtw_id = unique_list_dev[1]
for index, row in devicedf.iterrows():
    if(row['gtw_id'] != gtw_id):
        deletion_list.append(index)
    
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax2 = toscatterplot.plot(x='received', y='humidity', c='#FF0000', style = '.', title = 'Packets sent by static_7_02', grid=True, ax=ax1)
ax2.legend([unique_list_dev[0], unique_list_dev[1]])
ax2.set_xlabel("Time")            
ax2.set_ylabel("Pressure (Pa)")        
'''

'''   
toscatterplot=toscatterplot.drop(labels = deletion_list, axis = 0)
toscatterplot=toscatterplot.reset_index(drop=True)
ax1 = toscatterplot.plot(x='received', y='rssi', c='#0000FF', style = '.',  title = 'Packets sent by static_6_02', grid=True)
ax1.legend([unique_list_dev[0]])
ax1.set_xlabel("Time")            
ax1.set_ylabel("RSSI (dBm)")      
'''

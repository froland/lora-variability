# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:48:32 2019

@author: Nikola
"""
####
#### Calcul de la matrice de Pearson pour déterminer les corrélations entre les variables
####

#import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
#from datetime import datetime #Cela aiderait pour manipuler les  timestamp ... (à vérifier)

pkgw=pd.read_csv('pk-gw-dummy.csv', sep=';')
weather=pd.read_csv('weather.csv', sep=';')

pkgw = pkgw.sort_values(by = 'timestmp') #ordonner le DF selon la colonne des timestamps
#gwload=gwload.sort_values(by = 'gw_id')

# For dropping columns of dataframe pkgw.drop(["dev_eui", "gw_id", "timestmp", "cr","freqband","counter", "dev_lat","dev_long", "dev_alt"], axis = 1, inplace = True)
pkgw = pkgw[["rssi", "snr", "sf", "pld_size", "power_tx", "dev_alt"]] #To keep only specific columns that I want
pdpearson=pkgw.corr(method='pearson')


weather = weather[["temp_3m", "temp_30m","wnd_spd","wnd_drct","rain_quan"]]
bigdata = pd.concat([pkgw, weather], axis = 1,ignore_index = False)
pdpearson2 = bigdata.corr(method = 'pearson')
#Note = using correlation with the panda library (dataframe.corr) is more forgiving with the "nan" values !

####
#### Tracé de graphiques (avec un axe y à gauche et à droite)
####

pkgw=pd.read_csv('pk-gw-dummy.csv', sep=';')
weather=pd.read_csv('weather.csv', sep=';')

pkgw = pkgw.sort_values(by = 'timestmp') #ordonner le DF selon la colonne des timestamps
#gwload=gwload.sort_values(by = 'gw_id')

pkgw = pkgw[["rssi","timestmp"]]
weather = weather[["temp_3m", "timestmp"]]
graph = pd.concat([pkgw, weather], axis = 0, ignore_index = False, sort = False)
graph=graph.sort_values(by ='timestmp')


ax=graph.plot(kind='line', x='timestmp', y='temp_3m', xlim=[1552863600,1552953600], color='DarkBlue', style='.', markersize=5, label='temp_3m (blue)')
graph.plot(kind='line', x='timestmp', y='rssi', secondary_y=True, color='Red', style='.', markersize=5, label='rssi (red)', ax=ax);


####
#### Calcul des distances entre une gateway et un end-device
####

from haversine import haversine

pkgw=pd.read_csv('pk-gw-dummy.csv', sep=';')
gwloc=pd.read_csv('gateway_location.csv', sep=';')


dev_location = pkgw[["dev_lat", "dev_long", "dev_alt"]]
dev_location = dev_location.values
gw_location = gwloc[["gw_lat", "gw_long", "gw_alt"]]
gw_location = gw_location.values


loc1 = (dev_location[1,0], dev_location[1,1])
loc2 = (gw_location[1,0], gw_location[1,1]) #Could put these lines in a loop

hav = haversine(loc1, loc2) #distance in kilometers
hav=hav*1000 #distance in meters
distance = (hav**2 + (dev_location[1,2]-gw_location[1,2])**2)**(0.5) #in meters
#----------
#On peut calculer la distance entre un noeud mobile et la gateway sur laquelle il a transmis ses données et comparer
#l'évoltuion de cette distance par rapport à la variation de RSSI/SNR.
#Il est plus pertinent de regarder la variation de distance chez les noeuds mobiles que les noeuds fixes.
#" L'augmentation du Spreading Factor permet de couvrir une distance 
#plus grande entre l'équipement et la passerelle au détriment de la bande passante disponible."
# https://fr.wikipedia.org/wiki/LoRaWAN#Modulation_LoRa
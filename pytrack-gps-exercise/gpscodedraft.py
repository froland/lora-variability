import numpy as np
from micropyGPS import MicropyGPS
import binascii

my_gps = MicropyGPS()

latitude = my_gps.latitude
longitude = my_gps.longitude
altitude = my_gps.altitude

latitude = (51, 25.5, 'N')
longitude = (4, 48.8, 'E')
altitude = 42

deg_lat = latitude[0] - 50
decimal_lat = np.int32(10000*latitude[1]/60)
bin_deg_lat = format(deg_lat, 'b')
bin_dec_lat = format(decimal_lat, 'b')

deg_long = longitude[0]-3
decimal_long = np.int32(10000*longitude[1]/60)
bin_deg_long = format(deg_long, 'b')
bin_dec_long = format(decimal_long,'b')

altitude = np.int16(altitude)
bin_alt = format(altitude, 'b')

list_deg_lat = ['0']*1
list_dec_lat = ['0']*14

list_deg_long = ['0']*2
list_dec_long = ['0']*14

list_alt = ['0']*9

list_deg_lat[0] = bin_deg_lat

n = len(list_dec_lat)-1
for i in reversed(range(len(bin_dec_lat))):
    list_dec_lat[n] = bin_dec_lat[i]
    n = n - 1

n = len(list_deg_long) - 1
for i in reversed(range(len(bin_deg_long))):
    list_deg_long[n] = bin_deg_long[i]
    n = n - 1    

n = len(list_dec_long) - 1
for i in reversed(range(len(bin_dec_long))):
    list_dec_long[n] = bin_dec_long[i]
    n = n - 1    

n = len(list_alt)-1
for i in reversed(range(len(bin_alt))):
    list_alt[n] = bin_alt[i]
    n = n - 1
    
coord = list_alt + list_dec_lat + list_deg_lat + list_dec_long + list_deg_long
# 9 bits for altitude - 14 bits for decimal latitude - 1 bit for degree latitude -> 
# -> 14 bits for decimal longitude - 2 bits for degree longitude 
# 9b + 14b + 1b + 14b + 2b = 40 bits = 5 bytes
coord = ''.join(coord)
print(coord)
coord = hex(int(coord,2))[2:]
print(coord)
coord = bytearray.fromhex(coord) #Byte array
print(coord)

# Converting back to check if it is still correct
coord = binascii.hexlify(coord)
print(coord)
coord = bin(int(coord,16))[2:]
print(coord)
import numpy as np
from micropyGPS import MicropyGPS

def GPScoords():
    """This function uses the Micropygps library to get GPS coordinates
    and altitude from the GPS chip of the Pytrack expansion board and 
    returns a byte array that can be sent by the buffer of a LoRa transmission.
    The format of the data is the following (field size is in bits): 
    altitude(9) - latitude decimal (14) latitude degree (1) - longitude decimal (14) - degree decimal (2)
    The total amount of bits is 40, which makes 5 bytes to send.
    NOTE1: The decimal values must be divided by 10000 at the reception and added to the degree part.
    NOTE2: At the recepetion, latitude = latitude+50 and longitude = longitude + 3 """
    
    my_gps = MicropyGPS()

    #Fetching the coordinates and the altitude from the GPS chip
    latitude = my_gps.latitude
    longitude = my_gps.longitude
    altitude = my_gps.altitude
    
    #Optimising data representation (latitutde)
    deg_lat = latitude[0] - 50 #The experiment area's latitude varies from 50° to 51° (Belgium)
    decimal_lat = np.int32(10000*latitude[1]/60) #Conversion of decimal minutes in decimals and multiplication by 10000
    #Getting binary representation of the data
    bin_deg_lat = format(deg_lat, 'b')
    bin_dec_lat = format(decimal_lat, 'b')

    #Optimising data representation (longitude)
    deg_long = longitude[0]-3 #The experiment area's longitude varies from 3° to 6° (Mons-Namur approx.)
    decimal_long = np.int32(10000*longitude[1]/60)  #Conversion of decimal minutes in decimals
    #Getting binary representation of the data
    bin_deg_long = format(deg_long, 'b')
    bin_dec_long = format(decimal_long,'b')

    #Altitude data optimisation
    altitude = np.int16(altitude)
    #Getting binary representation of the data
    bin_alt = format(altitude, 'b')

    #Creating fixed size lists for each data (the size is in bits)
    list_deg_lat = ['0']*1
    list_dec_lat = ['0']*14

    list_deg_long = ['0']*2
    list_dec_long = ['0']*14

    list_alt = ['0']*9

    #Putting the strings in the fixed size lists (LSB is on the top right)
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
    
    #Concatenating all the lists into one and transforming the binary data into a byte array
    coord = list_alt + list_dec_lat + list_deg_lat + list_dec_long + list_deg_long
    coord = ''.join(coord)
    coord = hex(int(coord,2))[2:]
    coord = bytearray.fromhex(coord)
    
    return(coord) #Return a byte array

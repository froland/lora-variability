# Data storage structure

## packet_gateway (pk_gw)
* dev_eui : table of 8 bytes
* counter : integer (increment when a new packet is sent from end-device)
* gw_id : string
* RSSI : integer (in dBm)
* SNR : integer
* timestamp : timestamp (time region - date - hour/min/sec/msec/µsec)
* frequency band : float (in MHz)
* SF : integer (from 7 to 12)
* payload_size : integer (in bytes)
* coding rate (symbols per bit)
* power_tx : integer (dBm)
* dev_latitude : float
* dev_longitude : float
* dev_altitude : integer

## weather
* timestamp (from the internet data flow) : timestamp (time region - date - hour)
* station_id : string
* station_latitude : float
* station_longitude : float
* temperature_3m : float (degree celsius)
* temperature_30m : float (degree celsius)
* wind_speed : float (m/s)
* wind_direction : integer (degree)
* wind_sect : string 
* rain_quantity : float (mm)
* (pm_10) 

## gateway_load
* gw_id : string
* timestamp : timestamp (time region - date - hour)
* n_uplink : integer
* n_downlink : integer

## device-gateway
* gw_id : string
* dev_eui : table of 8 bytes
* timestamp : timestamp 
* n_packet_sent : integer
* n_packet_received_gw : integer

## gateway_location
* gw_id : string
* gw_latitude : float
* gw_longitude : float
* gw_altitude : integer

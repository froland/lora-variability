# Data storage structure

## packet_gateway (pk_gw) : This structure represents the packet sent from the node, passing through the gateways (but only one packet will be taken by the network server) and arriving at the application server
* dev_eui : table of 8 bytes --> from node
* counter : integer (increment when a new packet is sent from end-device) --> from node
* gw_id : string --> from gateway (only one packet from one gateway will be considered by the network server)
* RSSI : integer (in dBm) --> from gateway
* SNR : integer --> from gateway
* timestamp : timestamp (time region - date - hour/min/sec/msec/µsec) --> from gateway
* frequency band : float (in MHz) --> from node (can also be read at the gateway)
* SF : integer (from 7 to 12) --> from node
* payload_size : integer (in bytes) --> from gateway (because we want the data + encryption + encapsulation)
* coding rate (symbols per bit) --> from the node
* power_tx : integer (dBm) --> from the node
* dev_latitude : float
* dev_longitude : float
* dev_altitude : integer --> The last 3 parameters are the nodes positions and are either known by user (fixed node) or sent via a GPS (useful for mobile nodes)

## weather : This data comes from the weather data flow (airquality)
* timestamp (from the internet data flow) : timestamp (time region - date - hour)
* station_id : string
* station_latitude : float
* station_longitude : float
* temperature_3m : float (degree celsius)
* temperature_30m : float (degree celsius)
* atmospheric_pressure : float (Pa) (information will come from the "Super-Node")
* Air_humidity : integer (percentage) (information will come from the "Super-Node")
* wind_speed : float (m/s)
* wind_direction : integer (degree)
* wind_sect : string (e.g : NW, ESE, ...)
* rain_quantity : float (mm)
* (pm_10) 

## gateway_load : This data comes from the gateways and represents how many uplinks and downlinks (in total) each gateway has performed
* gw_id : string
* timestamp : timestamp (time region - date - hour)
* n_uplink : integer (from end-device to Network)
* n_downlink : integer (from Network to end-device)

## device-gateway : This structure shows how many packets were sent by a specific node and how many packets the gateway sent to this node
* gw_id : string
* dev_eui : table of 8 bytes
* timestamp : timestamp 
* n_packet_sent : integer
* n_packet_received_gw : integer

## gateway_location : This data adds the GPS coordinates of the gateways. The coordinates are known and computed in the TTN console
* gw_id : string
* gw_latitude : float
* gw_longitude : float
* gw_altitude : integer

## free_days : This table simply represents the legal free days in our country (it may vary from one year to another)
* date : date

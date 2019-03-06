# Data storage structure

## packet_gateway (pk_gw)
* dev_eui : table of 8 bytes
* counter : integer (increment when a new packet is sent from end-device)
* port : integer
* gw_id : string
* RSSI : integer (in dBm)
* SNR : integer
* timestamp : timestamp (time region - date - hour/min/sec)
* frequency band : float (in MHz)
* SF : integer (from 7 to 12)

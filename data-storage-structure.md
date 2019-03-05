# Data storage structure


# Second draft

## end_device

* app_name : string
* dev_id : string
* dev_addr : bytes
* dev_eui : bytes
* app_eui : bytes
* frequency : integer
* airtime : integer
* timestamp : integer
* rssi : integer
* snr : integer
* payload : bytes/float/integer
* SF : integer (from 7 to 12)


## gateway

* app_name : string
* gtw_id : string
* dev_addr : bytes
* dev_eui : bytes
* app_eui : bytes
* frequency : integer
* code rate : string
* SF : integer (from 7 to 12)
* BW : integer
* payload size : integer (ex : 16 bytes, where 16 is the integer)
* timestamp : string
* rssi : integer
* snr : integer


# First draft

## packet_enddevice

* dev_eui : bytes
* app_eui : bytes
* SF : integer (from 7 to 12)
* BW : integer
* gateway_id : string
* RSSI : integer
* SNR : integer (in dBm)
* timeslot : integer
* time : string
* frequency : integer
* data rate : string
* coding rate : string
* payload : integer or float (degree celsius, atm, ppm, ...) --> The environnmental parameter measured

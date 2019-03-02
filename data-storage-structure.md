# Data storage structure

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

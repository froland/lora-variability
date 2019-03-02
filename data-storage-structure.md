# Data storage structure

## packet_enddevice

* dev_eui : bytes
* SF : integer (from 7 to 12)
* BW : integer
* gateway_id : string
* RSSI : integer
* SNR : integer (in dB)
* timeslot : integer
* payload : integer or float (degree celsius, atm, ppm, ...) --> The environnmental parameter measured

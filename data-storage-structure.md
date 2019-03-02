# Data storage structure

## packet_enddevice

* dev_eui : bytes
* SF : integer (from 7 to 12)
* BW : integer
* gateway_id : string
* RSSI : integer
* SNR : integer (in dB)
* timeslot : integer (Can we know the time of the day with this ?)
* payload : integer or float (degree celsius, atm, ppm, ...) --> The environnmental parameter measured

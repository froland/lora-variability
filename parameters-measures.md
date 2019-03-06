# Parameters to measure

## External/environmental parameters

* Temperature (from weather data flow)
* Rain quantity (from weather data flow)
* Humidity of air (from weather data flow)
* Solar radiation (check with M. Roland)
* Atmospheric pressure (from weather data flow)
* Wind speed and direction (from weather data flow)
* Airborne particulate matter (check with M. Roland)


## Internal end-device parameters

* RSSI
* SNR
* Timestamp
* Frequency band
* CR (coding rate)
* SF (spreading factor)
* Payload size
* Emission power (if we can get it and transmit it - transmit the previous power(s) in the next packet(s) - store the values in non-volatile memory)


# Parameters that could be computed from measures

* Packet reception rate
* (Packet error rate)
* Gateway reception datarate
* (To discuss) Daytime/nighttime measures
* Week-end, working period, holidays
* Season of the year


# Outputs : how to represent the data (graph, stastitics, ...)

* Pearson correlation matrix
* RSSI as a function of the temperature, solar radiation, rain quantity, ...
* (RSSI with different spreading factors)
* (Probability density function of RSSI/SNR values of the received frames, as reported by gateways)
* (To discuss) Histogram of the used SF 
* RSSI as a function of the distance between the end-device and the gateway
* SNR as a function of the distance between the end-device and the gateway

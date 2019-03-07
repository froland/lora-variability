# Parameters to measure

## External/environmental parameters

* Temperature (from weather data flow)
* Rain quantity (from weather data flow)
* Humidity of air (from weather data flow) -- not available yet
* Atmospheric pressure (from weather data flow)
* Wind speed and direction (from weather data flow)
* Wind sector (from weather data flow)


## Internal end-device parameters

* RSSI (from the gateways)
* SNR (from the gateways)
* Timestamp (from the gateways)
* Frequency band (from the gateways)
* CR (coding rate) (from the gateways)
* SF (spreading factor) (from the gateways)
* Payload size (from the gateways)
* Emission power (if we can get it and transmit it - transmit the previous power(s) in the next packet(s) - store the values in non-volatile memory)


## Parameters that could be computed from measures (Nikola)

* Packet reception rate
* Packet error rate
* Gateway reception datarate
* Daytime/nighttime measures
* Week-end, working period, holidays --> Need a structure to know when it is a free day (jour férié légal)
* Season of the year


# Outputs : how to represent the data (graph, stastitics, ...)

* Pearson correlation matrix
* RSSI/SNR as a function of the temperature, rain quantity, ...
* SNRmargin (for ADR)
* RSSI/SNR as a function of the distance between the end-device and the gateway

# Parameters to measure

## External/environmental parameters

* Temperature (from weather data flow)
* Rain quantity (from weather data flow)
* Humidity of air (from weather data flow) -- not available yet
* Atmospheric pressure (from weather data flow) -- not available yet
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

* Packet reception rate (received packets/total number of sent packets) --> Each end-device has a counter that increments when a packet is sent (= total number of sent packets). In the "pk_gw" structure, we can identify the end-device with its dev_eui and check how many times there is an occurence of it in the table and compare that number with the counter.
* Gateway reception rate (total number of packets received over a period of time) --> We just have to look at how many packets were received during one hour (for example) at a gateway.
* Daytime/nighttime --> Need to look at the timestamp and classify them as "day" or "night"
* Week-end, working period, holidays --> Structure "free_days"
* Season of the year
* Distance between end-device and gateway (computed with coordinates of both) : http://boulter.com/gps/distance/?from=42.990967+-71.463767&to=40+-70&units=k


# Outputs : how to represent the data (graph, stastitics, ...)

* Pearson correlation matrix
* RSSI/SNR as a function of the temperature, rain quantity, ...
* SNRmargin (for ADR)
* RSSI/SNR as a function of the distance between the end-device and the gateway

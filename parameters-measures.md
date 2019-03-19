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
* Emission power (if we can get it and transmit it - transmit the previous 3 powers in the next packets - store the values in non-volatile memory. We transmit the last 3 powers because there is a risk of packet loss - if I my actual packet is sent but doesn't arrive, I will get the transmission power in the next packets)


## Parameters that could be computed from measures (Nikola)

* Packet reception rate (received packets/total number of sent packets) 
--> Each end-device has a counter that increments when a packet is sent (= total number of sent packets). In the "pk_gw" structure, we can identify the end-device with its dev_eui and check how many times there is an occurence of it in the table and compare that number with the counter. REMARK : BEFORE SENDING THE PACKET, THE COUNTER VALUE MUST BE AT 0. Drawback : if I reset my node (for any reason), I need to know if the counter has reset or not, to be able to carry on properly with the counting.
--> Total = cnt_max - cnt_min (ex: 257 - 253). This method works well if the counter is never reset. We can always know how many packets were sent from the end-device (in total)
--> We know how many packets we send over a period of time. This method is quiet simple, but not reliable. If the batteries of an end-device run out, we have to know exactly at what moment it happened to determine precisely how many packets were sent during the node's active period (when it was powered).
* Gateway reception rate (total number of packets received over a period of time) --> We just have to look at how many packets were received during one hour (for example) at a gateway.
* Business hours --> Need to look at the timestamp and classify them as "work" or "sleep" (8-17)
* Week-end, working period, holidays --> Structure "free_days"
* Season of the year (standard dates of each season)
* Distance between end-device and gateway (computed with coordinates of both) --> We can use the haversine function to compute the distance of two points on a sphere. After that, we can compute the real distance by considering the difference of altitude between the 2 points (Pythagore's formula)


# Outputs : how to represent the data (graph, stastitics, ...)

* Pearson correlation matrix
* RSSI/SNR as a function of the temperature, rain quantity, ...
* SNRmargin (for ADR)
* RSSI/SNR as a function of the distance between the end-device and the gateway

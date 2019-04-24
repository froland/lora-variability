# Payload conversion

We want to use the smallest payload to convey the more precise data.
We also want to keep precision to reasonable values regarding our use case, that is, measuring positions with a GPS chipset with a 2.5m accuracy.

## Battery voltage

* battery_payload = round((battery_voltage - 3.0) x 500.0)
* battery_voltage = (battery_payload / 500.0) + 3.0
* payload size: 10 bits
* effective range: 3.0 V to 5.046 V
* effective precision: 0.002 V

## Latitude

* latitude_payload = round((latitude_degree - 49.5) * 30000.0)
* latitude_degree = (latitude_payload / 30000.0) + 49.5
* payload size: 16 bits
* effective range: 49.5000°N - 51.6845°N
* effective precision: 0.00003° ~ 3.7m

## Longitude

* longitude_payload = round((longitude_degree - 2.545) * 20000.0)
* longitude_degree = (longitude_payload / 20000.0) + 2.545 
* payload size: 16 bits
* effective range: 2.545°E - 5.82175°E
* effective precision: 0.00005° ~ 3.58m 

## Horizontal dilution of precision

* hdop_payload = round(hdop_factor * 50.0)
* hdop_factor = hdop_payload / 50.0
* payload size: 10 bits
* effective range: 0 - 10.23
* effective precision: 0.02

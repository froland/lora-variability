# Payload conversion

We want to use the smallest payload to convey the more precise data.
We also want to keep precision to reasonable values regarding our use case, that is, measuring standard ambient conditions.

## Battery voltage

* battery_payload = round((battery_voltage - 3.0) x 500.0)
* battery_voltage = (battery_payload / 500.0) + 3.0
* payload size: 10 bits
* effective range: 3.0 V to 5.046 V
* effective precision: 0.002 V

## Temperature

* temperature_payload = round((temperature + 30.0) x 10.0)
* temperature = (temperature_payload / 10.0) - 30.0
* payload size: 10 bits
* effective range: -30.0 °C to  72.3 °C
* effective precision: 0.1°C

## Relative humidity

* humidity_payload = round(humidity x 2.0)
* humidity = humidity_payload / 2.0
* payload size: 8 bits
* effective range: 0.0 % to 127.5 %
* effective precision: 0.5 %

## Barometric pressure

* pressure_payload = round((pressure - 80000.0) / 7.0)
* pressure = (pressure_payload x 7.0) + 80000.0
* payload size: 12 bits
* effective range: 80000 Pa to 108665 Pa
* effective precision = 7 Pa

# InfluxDB data migration

## Before migration

**device_packet**

* 1 point par message reçu par une gateway
* Fields: counter, battery, temperature, humidity, pressure, rssi, snr
* Tags: coding_rate, data_rate, dev_eui, dev_id, frequency, gtw_id
* Clé unique: dev_id, gtw_id, counter (+ time si overflow ou reset counter)

## After migration

**environment**

* 1 point per sent message
* Tags: dev_id
* Fields: battery, temperature, humidity, pressure

**transmission**

* 1 point per received message per gateway
* Tags: dev_id, gtw_id, coding_rate, spreading_factor, bandwidth, frequency
* Fields: rssi, snr

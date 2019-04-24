#!/bin/bash
influx -execute 'SELECT first(battery) as battery, first(temperature) as temperature, first(humidity) as humidity, first(pressure) as pressure INTO lora_mons_environment FROM device_packet GROUP BY time(10m), dev_id' -host 'tsvisu.umons.ac.be' -database 'froland' -username '' -password '' -ssl
sudo influx_inspect export -database froland -datadir /var/lib/influxdb/data -waldir /var/lib/influxdb/wal -out ./export_influx
sudo chown froland:froland ./export_influx
sed -i -f migrate.sed ./export_influx
curl -i -u ':' -XPOST 'https://tsvisu.umons.ac.be:8086/write?db=froland&' --data-binary @./export_influx
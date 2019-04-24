/device_packet.*\(rssi\|snr\)/ !d
s/device_packet/lora_mons_transmission/
s/data_rate=SF/spreading_factor=/
s/BW/,bandwidth=/
s/dev_eui=[0-9A-F]\+,//
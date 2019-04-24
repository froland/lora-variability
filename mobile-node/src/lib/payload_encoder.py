def _convert_battery_voltage(input):
    return round((input - 3.0) * 500.0)


def _convert_latitude(input):
    return round((input - 49.5) * 30000.0)


def _convert_longitude(input):
    return round((input - 2.545) * 20000.0)


def _convert_hdop(input):
    return round(input * 100.0)

def encode(battery_voltage: float, latitude: float, longitude: float, hdop: float):
    payload = _convert_battery_voltage(battery_voltage) << 46
    payload += _convert_latitude(latitude) << 30
    payload += _convert_longitude(longitude) << 14
    payload += _convert_hdop(hdop) << 4
    payload += 0x0F
    return payload

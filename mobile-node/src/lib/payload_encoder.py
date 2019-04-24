def _convert_battery_voltage(input):
    return round((input - 3.0) * 500.0)


def _convert_temperature(input):
    return round((input + 30.0) * 10.0)


def _convert_humidity(input):
    return round(input * 2.0)


def _convert_pressure(input):
    return round((input - 80000.0) / 7.0)


def encode(battery_voltage: float, temperature: float, humidity: float, barometric_pressure: float):
    payload = _convert_battery_voltage(battery_voltage) << 30
    payload += _convert_temperature(temperature) << 20
    payload += _convert_humidity(humidity) << 12
    payload += _convert_pressure(barometric_pressure)
    return payload

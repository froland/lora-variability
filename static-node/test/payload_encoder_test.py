import payload_encoder


def test_encode():
    payload_bytes = payload_encoder.encode(4.766989, 26.34879, 33.79111, 102286.5)
    assert len(payload_bytes) == 5
    payload = int.from_bytes(payload_bytes, byteorder='big', signed=False)
    decoded_battery = payload >> 30
    assert decoded_battery == 883
    decoded_temperature = (payload >> 20) & 0b1111111111
    assert decoded_temperature == 563
    decoded_humidity = (payload >> 12) & 0b11111111
    assert decoded_humidity == 68
    decoded_pressure = payload & 0b111111111111
    assert decoded_pressure == 3184

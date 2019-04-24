import payload_encoder


def test_encode_full():
    payload = payload_encoder.encode(4.766989, 50.446150, 3.956785, 1.25)
    decoded_battery = payload >> 46
    assert decoded_battery == 883
    decoded_latitude = (payload >> 30) & 0b1111111111111111
    assert decoded_latitude == 28385
    decoded_longitude = (payload >> 14) & 0b1111111111111111
    assert decoded_longitude == 28236
    decoded_hdop = (payload >> 4) & 0b1111111111
    assert decoded_hdop == 125


def test_encode_battery():
    payload = payload_encoder.encode(4.766989)
    decoded_battery = payload >> 6
    assert decoded_battery == 883

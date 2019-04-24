function Decoder(bytes, port) {
  var decoded = {};

  if (port === 2) {
    var battery_payload = (bytes[0] << 2) + (bytes[1] >> 6);
    decoded.battery = (battery_payload) / 500.0 + 3.0;
    var latitude_payload = ((bytes[1] & 0x3F) << 10) + (bytes[2] << 2) + (bytes[3] >> 6);
    decoded.latitude = (latitude_payload / 30000.0) + 49.5;
    var longitude_payload = ((bytes[3] & 0x3F) << 10) + (bytes[4] << 2) + (bytes[5] >> 6);
    decoded.longitude = (longitude_payload / 20000.0) + 2.545;
    var hdop_payload = ((bytes[5] & 0x3F) << 4) + (bytes[6] >> 4);
    decoded.hdop = hdop_payload / 100.0;
  }

  if (port === 3) {
    var battery_payload = (bytes[0] << 2) + (bytes[1] >> 6);
    decoded.battery = (battery_payload) / 500.0 + 3.0;
  }

  return decoded;
}

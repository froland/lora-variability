function Decoder(bytes, port) {
  var decoded = {};

  if (port === 2) {
    var battery_payload = (bytes[0] << 2) + (bytes[1] >> 6);
    decoded.battery = (battery_payload) / 500.0 + 3.0;
    var temperature_payload = ((bytes[1] & 0x3F) << 4) + (bytes[2] >> 4);
    decoded.temperature = (temperature_payload / 10.0) - 30.0;
    var humidity_payload = ((bytes[2] & 0x0F) << 4) + (bytes[3] >> 4);
    decoded.humidity = humidity_payload / 2.0;
    var pressure_payload = ((bytes[3] & 0x0F) << 8) + bytes[4];
    decoded.pressure = (pressure_payload * 7.0) + 80000.0;
  }

  return decoded;
}

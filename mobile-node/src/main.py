import machine
import gc
from time import sleep

DEBUG = False

try:
    import config
    import pycom
    from micropython import const
    from pytrack import Pytrack
    from micropyGPS import MicropyGPS
    import payload_encoder
    from ttn_client import TtnClient
    from datarate_selector import select_datarate

    WAIT_FOR_LORA_S = const(30)
    WAIT_FOR_GPS_S = const(30)
    SLEEP_TIMEOUT_S = const(600)
    GPS_I2CADDR = const(0x10)

    # Colors
    OFF = const(0x000000)
    VIOLET = const(0x9400D3)
    INDIGO = const(0x4B0082)
    BLUE = const(0x0000FF)
    GREEN = const(0x00FF00)
    YELLOW = const(0xFFFF00)
    ORANGE = const(0xFF7F00)
    RED = const(0xFF0000)

    pycom.wifi_on_boot(False)
    pycom.wdt_on_boot(False)
    pycom.heartbeat(False)
    if DEBUG:
        pycom.rgbled(VIOLET)
        print("Collecting environment data")
    py = Pytrack()
    gps = MicropyGPS(location_formatting='dd')

    # Stop logging to local flash of GPS
    py.i2c.writeto(GPS_I2CADDR, "$PMTK185,1*23\r\n")
    py.i2c.writeto(GPS_I2CADDR, bytes([0]))
    # Use GPS, GONASS, GALILEO and GALILEO Full satellites, disable Beidou
    py.i2c.writeto(GPS_I2CADDR, "$PMTK353,1,1,1,1,0*2B\r\n")
    py.i2c.writeto(GPS_I2CADDR, bytes([0]))
    # Increase output rate to 5Hz (max with currently activated satellites)
    py.i2c.writeto(GPS_I2CADDR, "$PMTK220,200*2C\r\n")
    py.i2c.writeto(GPS_I2CADDR, bytes([0]))

    if DEBUG:
        pycom.rgbled(VIOLET)
        print("reading GPS data...")

    chrono = machine.Timer.Chrono()
    chrono.start()

    latitude = None
    longitude = None
    hdop = None
    fixed = False
    raw = bytearray(1)
    gc.enable()
    while True:
        raw = py.i2c.readfrom(GPS_I2CADDR, 128)
        for b in raw:
            sentence = gps.update(chr(b))
            if sentence is not None:
                if gps.satellite_data_updated() and gps.fix_type > 1:
                    if DEBUG:
                        print("Got a GPS fix: " + str(gps.fix_type) + "D")
                    latitude = gps.latitude[0]
                    longitude = gps.longitude[0]
                    hdop = gps.hdop
                    fixed = True
        if fixed or chrono.read() > WAIT_FOR_GPS_S:
            break
        sleep(0.2)
    gc.disable()
    chrono.stop()
    chrono.reset()

    battery = py.read_battery_voltage()

    if DEBUG:
        print("Battery voltage =", battery, "V")
        print("Latitude =", latitude, "°N")
        print("Longitude =", longitude, "°N")
        print("HDOP =", hdop)
        pycom.rgbled(INDIGO)
        print("Initializing TTN client...")
    client = TtnClient(config.app_eui, config.app_key, WAIT_FOR_LORA_S, debug=DEBUG)
    if DEBUG:
        pycom.rgbled(BLUE)
        print("Sending payload...")
    payload = payload_encoder.encode(battery, latitude, longitude, hdop).to_bytes(7 if fixed else 2, 'big', False)
    counter = pycom.nvs_get('counter')
    if counter is None or counter > 65535:
        counter = 0
    datarate = select_datarate(counter)
    pycom.nvs_set('counter', counter + 1)
    client.send(payload, datarate, 2 if fixed else 3)
    if DEBUG:
        pycom.rgbled(GREEN)
        print("Going to sleep...")
    py.setup_sleep(SLEEP_TIMEOUT_S)
    py.go_to_sleep(gps=True)
    if DEBUG:
        pycom.rgbled(RED)
        print("This message should not be displayed")
except Exception as ex:
    print("!!! Exception detected !!!", type(ex), ex)
finally:
    if DEBUG:
        print("Trigger reset")
        sleep(1)
    machine.reset()

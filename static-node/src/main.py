import machine
from time import sleep

DEBUG = True

try:
    import config
    import pycom
    from micropython import const
    from pysense import Pysense
    from SI7006A20 import SI7006A20
    from MPL3115A2 import MPL3115A2, PRESSURE
    import payload_encoder
    from ttn_client import TtnClient

    WAIT_FOR_LORA_S = const(30)
    SLEEP_TIMEOUT_S = const(20)

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
    py = Pysense()
    mp = MPL3115A2(py, mode=PRESSURE)
    si = SI7006A20(py)
    battery = py.read_battery_voltage()
    temperature = si.temperature()
    humidity = si.humidity()
    pressure = mp.pressure()
    if DEBUG:
        print("Battery voltage =", battery, "V")
        print("Temperature =", temperature, "°C")
        print("Humidity =", humidity, "%")
        print("Pressure =", pressure, "Pa")
    if DEBUG:
        pycom.rgbled(INDIGO)
        print("Initializing TTN client...")
    client = TtnClient(config.app_eui, config.app_key, WAIT_FOR_LORA_S, debug=DEBUG)
    if DEBUG:
        pycom.rgbled(BLUE)
        print("Sending payload...")
    payload = payload_encoder.encode(battery, temperature, humidity, pressure)
    client.send(payload)
    if DEBUG:
        pycom.rgbled(GREEN)
        print("Going to sleep...")
    machine.deepsleep(SLEEP_TIMEOUT_S * 1000)
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

import machine
from time import sleep

try:
    import config
    import pycom
    from micropython import const
    from ttn_client import TtnClient

    DEBUG = True

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

    pycom.heartbeat(False)
    if DEBUG:
        pycom.rgbled(VIOLET)
        print("Initializing TTN client...")
    client = TtnClient(config.app_eui, config.app_key, WAIT_FOR_LORA_S, debug=DEBUG)
    if DEBUG:
        pycom.rgbled(BLUE)
        print("Sending payload...")
    client.send([])
    if DEBUG:
        pycom.rgbled(GREEN)
        print("Going to sleep...")
    machine.deepsleep(SLEEP_TIMEOUT_S * 1000)
except Exception as ex:
    print("!!! Exception detected !!!", type(ex), ex, flush=True)
finally:
    print("Trigger reset")
    sleep(1)
    machine.reset()

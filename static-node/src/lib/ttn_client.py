import socket
from binascii import unhexlify
from time import sleep

try:
    from network import LoRa
except ImportError:
    class LoRa:
        pass
try:
    from machine import Timer
except ImportError:
    class Timer:
        pass


class JoinException(Exception):
    pass


class TtnClient:
    def __init__(self, app_eui, app_key, join_timeout, debug=False):
        self.app_eui = unhexlify(app_eui)
        self.app_key = unhexlify(app_key)
        self.join_timeout = join_timeout
        self.debug = debug
        if self.debug:
            print("Turning on LoRa radio...")
        self.lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868, adr=False)
        if self.debug:
            print("Restoring state from NVRAM")
        self.lora.nvram_restore()

    def _join(self):
        if self.debug:
            print("Joining new session...")
        self.lora.join(activation=LoRa.OTAA, auth=(self.app_eui, self.app_key), timeout=0, dr=0)
        chrono = Timer.Chrono()
        while not self.lora.has_joined() and chrono.read() < self.join_timeout:
            if self.debug:
                print(".", end='')
            sleep(1)
        chrono.stop()
        if not self.lora.has_joined():
            if self.debug:
                print("Could not join a new session")
            raise JoinException
        else:
            if self.debug:
                print("Joined new session")

    def send(self, payload):
        if not self.lora.has_joined():
            self._join()
        s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, False)
        s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
        s.bind(1)
        s.setblocking(True)
        if self.debug:
            print("Sending payload...")
        s.send(payload)
        if self.debug:
            print("Payload sent")
        s.setblocking(False)
        if self.debug:
            print("Saving state to NVRAM...")
        self.lora.nvram_save()

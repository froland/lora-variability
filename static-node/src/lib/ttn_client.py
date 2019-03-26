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
    def __init__(self, app_eui, app_key, join_timeout):
        self.app_eui = unhexlify(app_eui)
        self.app_key = unhexlify(app_key)
        self.join_timeout = join_timeout
        self.lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868, adr=False)
        self.lora.nvram_restore()

    def _join(self):
        if not self.lora.has_joined():
            self.lora.join(activation=LoRa.OTAA, auth=(self.app_eui, self.app_key), timeout=0, dr=0)
            chrono = Timer.Chrono()
            while not self.lora.has_joined() and chrono.read() < self.join_timeout:
                sleep(1)
            chrono.stop()
            if not self.lora.has_joined():
                raise JoinException

    def send(self, payload):
        if not self.lora.has_joined():
            self._join()
        s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, False)
        s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
        s.bind(1)
        s.setblocking(True)
        s.send(payload)
        s.setblocking(False)
        self.lora.nvram_save()

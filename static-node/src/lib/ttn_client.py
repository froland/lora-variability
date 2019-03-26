try:
    from network import LoRa
except ImportError:
    class LoRa:
        pass
import socket
from binascii import unhexlify


class JoinException(Exception):
    pass


class TtnClient:
    def __init__(self, app_eui, app_key):
        self.lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868, adr=False)
        self.app_eui = unhexlify(app_eui)
        self.app_key = unhexlify(app_key)

    def join(self):
        self.lora.join(activation=LoRa.OTAA, auth=(self.app_eui, self.app_key), timeout=0, dr=0)
        if not self.lora.has_joined():
            raise JoinException

    def send(self, payload):
        if not self.lora.has_joined():
            self.join()
        s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        print(s)
        s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, False)
        s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
        s.bind(1)
        s.setblocking(True)
        s.send(payload)

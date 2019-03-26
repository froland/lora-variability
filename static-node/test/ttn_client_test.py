import unittest
from unittest.mock import patch
from ttn_client import TtnClient

APP_EUI = b'00112233445566'
APP_KEY = b'00112233445566778899AABBCCDDEEFF'
PAYLOAD = [0x00, 0x11, 0x22]


class DummyLoRa:
    def __init__(self, mode=None, region=None, adr=None):
        pass


@patch('ttn_client.LoRa')
class TtnClientTest(unittest.TestCase):
    def test_constructor(self, LoRa):
        client = TtnClient(APP_EUI, APP_KEY)

    @patch('ttn_client.socket')
    def test_send_payload(self, socketClass, LoRa):
        lora = LoRa.return_value
        lora.has_joined.side_effect = [False, False]
        socket = socketClass.socket.return_value
        client = TtnClient(APP_KEY, APP_KEY)
        client.send(PAYLOAD)
        lora.join.assert_called()
        socket.send.assert_called()


if __name__ == '__main__':
    unittest.main()

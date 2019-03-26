from unittest import TestCase
from unittest.mock import patch
from ttn_client import TtnClient, JoinException

APP_EUI = b'00112233445566'
APP_KEY = b'00112233445566778899AABBCCDDEEFF'
JOIN_TIMEOUT = 3
PAYLOAD = [0x00, 0x11, 0x22]


@patch('ttn_client.LoRa')
class TtnClientTest(TestCase):
    def test_constructor(self, LoRa):
        client = TtnClient(APP_EUI, APP_KEY, JOIN_TIMEOUT)

    @patch('ttn_client.Timer')
    @patch('ttn_client.socket')
    def test_send_payload(self, socketClass, Timer, LoRa):
        socket = socketClass.socket.return_value
        chrono = Timer.Chrono.return_value
        chrono.read.side_effect = [1, 2]
        lora = LoRa.return_value
        lora.has_joined.side_effect = [False, False, True, True]

        client = TtnClient(APP_EUI, APP_KEY, JOIN_TIMEOUT)
        client.send(PAYLOAD)

        lora.join.assert_called()
        socket.send.assert_called_with(PAYLOAD)
        lora.nvram_save.assert_called()

    @patch('ttn_client.sleep')
    @patch('ttn_client.Timer')
    @patch('ttn_client.socket')
    def test_send_timeout(self, socketClass, Timer, sleep, LoRa):
        socket = socketClass.socket.return_value
        chrono = Timer.Chrono.return_value
        chrono.read.side_effect = [1, 2, 3, 4]
        lora = LoRa.return_value
        lora.has_joined.return_value = False

        client = TtnClient(APP_EUI, APP_KEY, JOIN_TIMEOUT)
        with self.assertRaises(JoinException):
            client.send(PAYLOAD)

        lora.join.assert_called()
        socket.send.assert_not_called()
        lora.nvram_save.assert_not_called()

    @patch('ttn_client.socket')
    def test_send_with_recovered_session(self, socketClass, LoRa):
        socket = socketClass.socket.return_value
        lora = LoRa.return_value
        lora.has_joined.side_effect = [False, True]

        client = TtnClient(APP_EUI, APP_KEY, JOIN_TIMEOUT)
        client.send(PAYLOAD)

        lora.nvram_restore.assert_called()
        lora.join.assert_not_called()
        socket.send.assert_called_with(PAYLOAD)
        lora.nvram_save.assert_called()


if __name__ == '__main__':
    unittest.main()

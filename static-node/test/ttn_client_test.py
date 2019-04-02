from ttn_client import TtnClient, JoinException

APP_EUI = b'00112233445566'
APP_KEY = b'00112233445566778899AABBCCDDEEFF'
JOIN_TIMEOUT = 3
PAYLOAD = [0x00, 0x11, 0x22]


def test_constructor(mocker):
    mocker.patch('ttn_client.LoRa')
    client = TtnClient(APP_EUI, APP_KEY, JOIN_TIMEOUT)
    assert client is not None


def test_send_payload(mocker):
    LoRa = mocker.patch('ttn_client.LoRa')
    mocker.patch('ttn_client.sleep')
    Timer = mocker.patch('ttn_client.Timer')
    socketClass = mocker.patch('ttn_client.socket')
    socket = socketClass.socket.return_value
    chrono = Timer.Chrono.return_value
    chrono.read.side_effect = [1, 2]
    lora = LoRa.return_value
    lora.has_joined.side_effect = [False, False, True, True]

    client = TtnClient(APP_EUI, APP_KEY, JOIN_TIMEOUT)
    client.send(PAYLOAD)

    assert lora.join.called
    assert chrono.start.called
    socket.send.assert_called_with(PAYLOAD)
    assert lora.nvram_save.called


def test_send_timeout(mocker):
    from pytest import raises

    LoRa = mocker.patch('ttn_client.LoRa')
    mocker.patch('ttn_client.sleep')
    Timer = mocker.patch('ttn_client.Timer')
    socketClass = mocker.patch('ttn_client.socket')
    socket = socketClass.socket.return_value
    chrono = Timer.Chrono.return_value
    chrono.read.side_effect = [1, 2, 3, 4]
    lora = LoRa.return_value
    lora.has_joined.return_value = False

    client = TtnClient(APP_EUI, APP_KEY, JOIN_TIMEOUT)
    with raises(JoinException):
        client.send(PAYLOAD)

    assert lora.join.called
    socket.send.assert_not_called()
    lora.nvram_save.assert_not_called()


def test_send_with_recovered_session(mocker):
    LoRa = mocker.patch('ttn_client.LoRa')
    socketClass = mocker.patch('ttn_client.socket')
    socket = socketClass.socket.return_value
    lora = LoRa.return_value
    lora.has_joined.return_value = True

    client = TtnClient(APP_EUI, APP_KEY, JOIN_TIMEOUT)
    client.send(PAYLOAD)

    assert lora.nvram_restore.called
    lora.join.assert_not_called()
    socket.send.assert_called_with(PAYLOAD)
    assert lora.nvram_save.called

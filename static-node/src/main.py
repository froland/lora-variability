import config
import machine
import pycom
import usocket as socket
from micropython import const
from network import LoRa
from ubinascii import unhexlify
from ustruct import pack, calcsize
from utime import sleep

debug = True

wait_for_lora_s = const(30)
deep_sleep_timeout_s = const(20)
battery_min = 3.3
battery_max = 4.2
default_tx_power = const(14)

# Colors
off = const(0x000000)
blue = const(0x0000ff)
cyan = const(0x00ffff)
green = const(0x00ff00)
yellow = const(0xffff00)
red = const(0xff0000)
magenta = const(0xff00ff)

wdt_timeout = (wait_for_lora_s + 10) * 1000
#wdt = machine.WDT(timeout=wdt_timeout)


def join_ttn(lora):
  lora.nvram_restore()
  if not lora.has_joined():
    if debug:
      print("joining new TTN session...")
    app_eui = unhexlify(config.app_eui)
    app_key = unhexlify(config.app_key)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0, dr=0)
    chrono = machine.Timer.Chrono()
    while not lora.has_joined() and chrono.read() < wait_for_lora_s:
      sleep(5)
    chrono.stop()
    tx_power1 = lora.stats().tx_power
    pycom.nvs_set("tx_power1", tx_power1)
  return lora.has_joined()


def encode_payload():
  tx_power1 = pycom.nvs_get("tx_power1") or default_tx_power
  tx_power2 = pycom.nvs_get("tx_power2") or default_tx_power
  tx_power3 = pycom.nvs_get("tx_power3") or default_tx_power
  return pack('>BBB', tx_power1, tx_power2, tx_power3)


def send_to_ttn():
  lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868, adr=False)
  joined = join_ttn(lora)
  if (joined):
    msg = encode_payload()
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, False)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.bind(1)
    if debug:
      pycom.rgbled(cyan)
      print("sending LoRa message...")
    s.setblocking(True)
    s.send(msg)
    if debug:
      print("LoRa message sent")
    s.setblocking(False)
    if debug:
      print("receiving LoRa message...")
    data = s.recv(128)
    if debug and len(data) > 0:
      print("received data: " + str(data))
    tx_power = lora.stats()[6]
    if debug:
      print("tx_power was " + str(tx_power))
    tx_power1 = pycom.nvs_get("tx_power1") or default_tx_power
    tx_power2 = pycom.nvs_get("tx_power2") or default_tx_power
    tx_power3 = pycom.nvs_get("tx_power3") or default_tx_power
    if tx_power < 1:
      tx_power = tx_power1
    tx_power3 = tx_power2
    tx_power2 = tx_power1
    tx_power1 = tx_power
    pycom.nvs_set("tx_power1", tx_power1)
    pycom.nvs_set("tx_power2", tx_power2)
    pycom.nvs_set("tx_power3", tx_power3)
    lora.nvram_save()
  deep_sleep()


def deep_sleep():
  if debug:
    print("going to sleep...")
    pycom.rgbled(magenta)
  sleep(20)
  machine.reset()
  #machine.deepsleep(deep_sleep_timeout_s * 1000)


pycom.heartbeat(False)
pycom.rgbled(red)
#wdt.feed()
if debug:
  print("sending info to TTN...")
  pycom.rgbled(yellow)
send_to_ttn()
#wdt.feed()

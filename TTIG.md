# The Things Indoor Gateway

## Setup

1. Plug the gateway in.
2. Push and hold ```setup``` button for 10 seconds.
3. Connect to AP ```MiniHub-XXXXXX```.
4. Open http://192.168.4.1 in a browser.
5. Add your WiFi network SSID and key.
6. Save and reboot.
7. If the gateway manages to contact is configuration server, the WiFi LED will be steady green.

## Buttons

* SETUP button, 10s press: If in GW Mode: Switch to CONF Mode
* SETUP button, 5s press: If in CONF Mode: Reboot
* RESET button, 5s press: Factory reset (wipe out WiFi credentials and LNS credentials) - Caution: Factory reset requires resetting the credentials on the server side as well to authorize the gateway to fetch new personalized credentials.

## LED States

* GREEN - blinking 1 sec - [GW Mode] WiFi STA not connected
* GREEN - blinking 1/4 sec - [GW Mode] WiFi STA connected,establishing connection to LNS, configuring radio
* GREEN - solid - [GW Mode] WiFi STA connected, GW connected to LNS, radio listening
* GREEN/RED - blinking 1/4 sec - [GW Mode] WiFi STA connected, CONF transaction in progress. *NOTE: Do not unplug device in that state (possibly a firmware upgrade is in progress)*
* RED - blinking 1/4 sec - [CONF Mode] Scanning WiFi networks, setting up config AP
* RED - blinking 1 sec - [CONF Mode] Config AP active

## Further information

https://www.thethingsnetwork.org/forum/t/ttig-the-things-indoor-gateway/22049/43

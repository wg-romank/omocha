# Omocha

Simple remotely-controlled toy. Controller board is running a webserver to host UI for remote control.

Communication is done through WiFi. Wifi Configuration is stored in flash memory in file file called 'secret' in following format

```
<ssid>;<password>
```

Web UI is using [JoyStick](https://github.com/bobboteck/JoyStick/) minimalistic JavaScript library for joystick controller. Remote control logic is implemented on the client side to reduce amount of computation on the microcontroller as well as to make prototyping new UIs easier without need to re-flash the board.

Webserver is exposing single main endpoint

```bash
/set=?p4=<duty_p4>&p5=<duty_p5>
```

That sets respective duty values to control connected servos. Duty cycle calculation is also running on UI.

List of hardware:

- 1 x NodeMCU Esp-8266
- 2 x FS90R - continuous rotation servo
- 1 x TP4056 - battery charging / protection circuit
- 1 x Noname boost converter
- 1 x 360-mini DC-DC buck converter
- 1 x 1000mAh 1C 3.7v battery

Structural parts are created within OnShape and can be accessed throught [this link](https://cad.onshape.com/documents/6b025ad5b8d3cd7ed16cbb3e/w/f27e21178ea5a2d9bdf98c12/e/2fbd7fb4a6eb46e4acefeec9?renderMode=0&uiState=65a694ebbeed7c1f54f48a05).

Chasis parts were 3D printed in PLA, wheels - in TPU. Bottom parts have higher infil values to provide offset balance.

Wiring diagram

<TBD>

To build & flash firmware (MicroPython)

```bash
esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --verify --flash_size=4MB -fm dout 0 /path/to/esp-rom.bin
```

To wipe the board

```bash
esptool.py --port /dev/ttyUSB0 erase_flash
```

To flash code & static files (Web UI)

```bash
make
```

Tested with MicroPython build v1.18

## Future work

- Use web-sockets for control
  - currently UI makes HTTP request once every 200ms which is sub-optimal
- More sensors and full autonomy
- Wireless charging

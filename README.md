# Omocha

Simple remotely-controlled toy. Controller board is running a webserver to host UI for remote control.

Communication is done through WiFi. Wifi Configuration is stored in flash memory in file file called 'secret' in following format

```
<ssid>;<password>
```

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

# Omocha

To build & flash firmware (MicroPython)

```bash
esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --verify --flash_size=4MB -fm dout 0 ~/Downloads/ESP8266_GENERIC-20220117-v1.18.bin
```

To wipe the board

```bash
esptool.py --port /dev/ttyUSB0 erase_flash
```

To flash code

```bash
make
```

all:
	ampy -p /dev/ttyUSB0 put index.html
	ampy -p /dev/ttyUSB0 put secret
	ampy -p /dev/ttyUSB0 put main.py

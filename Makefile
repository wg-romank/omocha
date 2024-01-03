static:
	ampy -p /dev/ttyUSB0 put index.html
	ampy -p /dev/ttyUSB0 put secret
	ampy -p /dev/ttyUSB0 put joy.min.js

code:
	ampy -p /dev/ttyUSB0 put main.py

all: static code

.PHONY: static code all

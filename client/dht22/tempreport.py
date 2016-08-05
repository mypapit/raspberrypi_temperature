#!/usr/bin/python

import sys
import Adafruit_DHT


sensor = Adafruit_DHT.DHT22
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
	print('Temp {0:0.1f} Humidity {1:0.1f}%'.format(temperature, humidity))
	print (str(temperature) + " Celcius")
else:
	print('Failed to get reading. Try again!')
	sys.exit(1)


#!/usr/bin/python

import sys
import Adafruit_DHT
import pyttsx
import time
import requests

sensor = Adafruit_DHT.DHT22
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
	print('Temp {0:0.1f} Humidity {1:0.1f}%'.format(temperature, humidity))
	print (str(temperature) + " Celcius")
else:
	print('Failed to get reading. Try again!')
	sys.exit(1)

speech = pyttsx.init()
speech.setProperty("rate",150)

speaktemp = "{:0.1f}".format(temperature)
speakhumid = "{:0.1f}".format(humidity)

text2speech = "Temperature  is " + speaktemp + " Celcius , and Humidity is  " + speakhumid + " percent"

try: 
	req = requests.post("http://logger.mypapit.net/pi/ambient.php",{'device': 'oldpi', 'temp': speaktemp,'humidity': speakhumid})
	speech.say("Connected to server.....")
	print (req.status_code,req.reason)

except:
	print "No connection to server"




speech.say(text2speech)
 

speech.runAndWait()

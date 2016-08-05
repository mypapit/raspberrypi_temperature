#!/usr/bin/python

import os
import requests
import pyttsx
import time

def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))




if __name__ == '__main__':
  res = getCPUtemperature()

  print res


  try:
	req = requests.post("http://logger.mypapit.net/pi/coretemp.php",{'device': 'oldpi', 'temp': res})
	print (req.status_code,req.reason)
	print "placebo..."
  except requests.ConnectionError:
	print "No connection to server"






  speech = pyttsx.init()

  speech.setProperty("rate",150)
  
  text2speech = "Core Temperature is "+res+" celcius"
  speech.say(text2speech)
  
  if float(res) > 55.0:
	alert="Alert, Core is too hot, cooling is necessary"
        speech.say(alert)
	print "hot hot hot"

  speech.runAndWait()
  

  








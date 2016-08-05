#!/usr/bin/python

import os
import requests

def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))




if __name__ == '__main__':
  res = getCPUtemperature()

  req = requests.post("http://192.168.1.40/pi/updatecpu.php",{'device': 'oldpi', 'temp': res})
  print (req.status_code,req.reason)

  print res

#!/usr/bin/python

import os

def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))




if __name__ == '__main__':
  res = getCPUtemperature()
  print res

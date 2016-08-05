#!/usr/bin/python

#import httplib, urllib

import requests


#params = urllib.urlencode({'device': 'oldpi', 'temp': 47.5})
#headers ={"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
#conn = httplib.HTTPConnection("192.168.1.40/pi/updatecpu.php")
#conn.request("POST",params,headers)
#response = conn.getresponse()
#print response.status, response.reason
#conn.close()


req = requests.post("http://192.168.1.40/pi/updatecpu.php",{'device': 'oldpi', 'temp': 47.5})
print (req.status_code,req.reason)



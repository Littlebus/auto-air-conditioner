from urllib import request
import socket
import re
import time

apikey = '85b0c7f75ce26bdba4b5d16e64dd31d8'
url = 'http://api.yeelink.net/v1.0/device/355310/sensor/401858/datapoints'

def getSwitch(apikey,url):
	req = request.Request(url)
	req.add_header('U-ApiKey',apikey)
	res = request.urlopen(req).read().decode('ascii')
	status = int(re.findall(',"value":([0-9]+)',res)[0])
	return status

def controller(command):
	# now do some decode or issue relative command
	print("get command %d"%command)
	pass

	# 0 stand for shutdown
now = 0
while True:
	command = getSwitch(apikey,url)
	if not now == command:
		now = command
		controller(command)


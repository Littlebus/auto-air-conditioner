from urllib import request
import re
import time

def getTemp():

	try:
		tfile = open("/sys/bus/w1/devices/28-0316a0fc60ff/w1_slave")
	except Exception as e:
		print(e)
	else:
		text = tfile.read()
	finally:
		tfile.close()
	temperaturedata = re.findall(' t\=(\S+)$', text)
	temperature = float(temperaturedata[0]) / 1000
	return temperature

apikey = '85b0c7f75ce26bdba4b5d16e64dd31d8'
url = 'http://api.yeelink.net/v1.0/device/355310/sensor/401857/datapoints'
req = request.Request(url)
req.add_header('U-ApiKey',apikey)

while True:
	temperature = getTemp()
	value = '{"value":%f}' % temperature
	values = bytes(value.encode('utf8'))
	try:
		request.urlopen(req,data=values)
	except Exception as e:
		print('link error')
		print(e)
	else:
		print('link succeed')
	time.sleep(12)
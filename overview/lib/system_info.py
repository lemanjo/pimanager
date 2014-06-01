#system_info.py
import socket
from datetime import timedelta, datetime

def gethostname():
	return socket.gethostname()

def getuptime():
	with open('/proc/uptime', 'r') as f:
		uptime_seconds = float(f.readline().split()[0])
		uptime_string = str(timedelta(seconds = uptime_seconds))

	return uptime_string[:uptime_string.find(".")]

def getsystemtime():
	return datetime.now()
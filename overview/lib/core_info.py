#core_info.py
import psutil

def getcpuusage():
	return int(psutil.cpu_percent())

def getmemusage():
	return int(psutil.virtual_memory().percent)
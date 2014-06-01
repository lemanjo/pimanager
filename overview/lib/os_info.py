#os_info.py
import platform

def getplatform():
	return platform.uname()

def getdistro():
	return platform.dist()
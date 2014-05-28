# timezone.py
import time

# Returns server configured timezone
def gettz():
	if time.daylight:
		offsetHour = time.altzone / 3600
	else:
		offsetHour = time.timezone / 3600
	return 'Etc/GMT%+d' % offsetHour
from django.shortcuts import render
from django.template import Template, Context

# Custom imports
from pimanager.lib.is_sudo import is_sudo
from overview.lib.system_info import *
from overview.lib.os_info import *
from overview.lib.core_info import *
# Create your views here.

def home(request):
	platform = getplatform()
	contexts = {
		"hostname": gethostname(),
		"uptime": getuptime(),
		"system_time": getsystemtime(),
		"os": platform[0],
		"kernel": platform[2],
		"distro": getdistro(),
		"cpu_usage": getcpuusage(),
		"mem_usage": getmemusage(),
	}

	return render(request, 'overview.html', contexts)
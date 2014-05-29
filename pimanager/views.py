# views.py
from django.shortcuts import render
from django.template import Template, Context

from pimanager.lib.is_sudo import is_sudo

def home(request):
	contexts = {
		"is_sudo": is_sudo(request.user)
	}

	return render(request, 'home.html', contexts)
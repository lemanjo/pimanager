# views.py
from django.shortcuts import render
from django.template import Template, Context

from pimanager.lib.is_sudo import is_sudo

def home(request):
	return render(request, 'home.html')
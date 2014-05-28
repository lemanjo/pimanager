# views.py
from django.shortcuts import render
from django.template import Template, Context

def home(request):
	return render(request, 'home.html')
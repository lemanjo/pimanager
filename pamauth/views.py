from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from lib.pamauth import pam_authenticate

# Create your views here.
def login_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('home/')

	state = ""
	username = ""
	password = ""
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		# Compare system users to users in DB
		if not pam_authenticate(username=username, password=password):
			state = "Incorrect username or password."

		else:
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('home/')
				else:
					state = "Your account is not active, please contact the site admin."

			else:
				state = "Incorrect username or password."

	return render(request,"login.html",RequestContext(request,{'state':state, 'username': username}))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

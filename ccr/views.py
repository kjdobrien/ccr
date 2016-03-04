from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.template import RequestContext 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
	c ={}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/ccrform/user_profile')
		else:
			return HttpResponse("Invalid1")

	else:	
		return render_to_response('invalid.html')		

@login_required
def loggedin(request):
	return render_to_response('/accounts/loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('invalid.html')

def logout_view(request):
	logout(request)
	return render_to_response('logout.html')



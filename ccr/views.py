from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.template.context_processors import csrf
from django.template import RequestContext 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	
	if user is not None:
		messages.success(request, 'Login Successful')
		authenticate.login( request, user)
		return HttpResponseRedirect('/ccrform/')
	else:	
		return HttpResponseRedirect('/accounts/invalid')

@login_required
def loggedin(request):
	return render_to_response('loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('invalid.html')

def logout(request):
	logout(request)
	return render_to_response('logout.html')



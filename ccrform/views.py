from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404 
from django import forms 
from django.core.mail import send_mail
from django.template import RequestContext
#from ccrform.managers import User 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.context_processors import csrf
from forms import CcrForm
from ccrform.models import Ccr, Revision  


# Create your views here.

#@login_required 
def index(request):
	return HttpResponse("Welcome to the Index") 
	
#@login_required
def create_ccr(request):
	if request.POST:
		form = CcrForm(request.POST)
		if form.is_valid():
			ccr = form.save(commit=False)
			ccr.entered_by = request.user 
			ccr.ccr_number = str(ccr.date) + str(ccr.id).zfill(4) 
			first_rev = Revision(edited_by=request.user,ccr_ref=ccr,status_ref=ccr.status,date=ccr.date)
			first_rev.save()
			#send_mail() to reviewer 
			form.save()
			return HttpResponseRedirect('ccr/'+str(ccr.id)+'/')
		else:
			form = CcrForm()
		args = {}
		args['form'] = form
		args.update(csrf(request))
		return render_to_response('ccr/create_ccr.html', args)
		
#@login_required	
def review_ccr(request, ccr_id):
	ccr = get_object_or_404(Ccr, pk=ccr_id)
	if request.POST:
		form = ReviewForm(request.POST or None, instance=ccr)
		if form.is_valid():
			ccr = form.save(commit=False)
			ccr.status = FOR_APPROVAL
			second_rev = Revision(edited_by=request.user, ccr_ref=ccr, status_ref=ccr.status, date=datetime.date)
			#send_mail() to approver 
			form.save()
			return HttpResponseRedirect('ccr/'+str(ccr.id)+'/')
	else:
		form = ReviewForm()
	args = {}
	args['form'] = form
	args.update(csrf(request))
	return render_to_response('ccrform/review_ccr', args) 

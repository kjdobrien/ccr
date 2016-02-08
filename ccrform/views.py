from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404 
from django import forms 
from django.core.mail import send_mail
from django.template import RequestContext
#from ccrform.managers import User 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.context_processors import csrf
from forms import CcrForm, EditCcrForm 
from ccrform.models import Ccr, Revision, STATUS_CHOICES


# Create your views here.

#@login_required 
def index(request):
	return HttpResponse("Welcome to the Index") 

#@login_required
def view_ccr(request, ccr_id):
	ccr = get_object_or_404(Ccr, pk=ccr_id)
	args = {}
	args['ccr'] = ccr
	return render(request, 'ccrform/view_ccr.html', args)


	
#@login_required
def create_ccr(request):
	if request.POST:
		form = CcrForm(request.POST)
		if form.is_valid():
			ccr = form.save(commit=False)
			ccr.entered_by = request.user 
			#send_mail() to reviewer 
			form.save()	
			ccr.ccr_number = str(ccr.date) +'-'+ str(ccr.id).zfill(4) 
			form.save()
			ccr_number = str(ccr.ccr_number) 
			return HttpResponseRedirect('/ccrform/ccr/'+ccr_number+'/')
	else:
		form = CcrForm()
	args = {}
	args['form'] = form
	args.update(csrf(request))
	return render_to_response('ccrform/create_ccr.html', args)
		
#@login_required
#@permission_required()	
def change_status(request, ccr_id):
	ccr = get_object_or_404(Ccr, pk=ccr_id)
	
	if "Approvers" in request.user.groups:
		form = ApproverStatusForm(request.POST or None, instance=ccr)
		#email = approver email 
	else:
		form = ReviewerStatusForm(request.POST or None, instance=ccr)
		#email = reviewer email 
	if request.POST: 
		if form.is_valid():
			ccr = form.save(commit=False)
			new_rev = Revision(edited_by=request.user, ccr_ref=ccr, status_at_rev=ccr.status, date=datetime.date)
			#send_mail() 
			form.save()
			return HttpResponseRedirect('ccr/'+str(ccr.id)+'/')
	else:
	
		args = {}
		args['form'] = form
		args.update(csrf(request))
		return render_to_response('ccrform/review_ccr', args)

#@login_required
def edit_ccr(request, ccr_id):
	ccr = get_object_or_404(Ccr, pk=ccr_id)
	form = EditCcrForm(request.POST or None, instance=ccr)
	args = {}
	args['ccr'] = ccr
	if request.POST:
		if form.is_valid():
			new_rev = Revision(edited_by=request.user, ccr_ref=ccr, status_at_rev=ccr.status, date=datetime.date)
			new_rev.save() 
			form.save()
			return HttpResponseRedirect('ccr/'+str(ccr.id)+'/')
 
	else:
		form = EditCcrForm()
	args['form'] = form 
	args.update(csrf(request))
	return render(request, 'ccrform/edit_ccr.html', args) 


#@login_required
def view_all_ccr(request):
	ccr_list = Ccr.objects.all()

	context = {'ccr_list' : ccr_list } 
	return render(request, 'ccrform/view_all_ccr.html', context)


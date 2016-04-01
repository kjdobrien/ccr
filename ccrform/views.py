from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response, get_object_or_404 
from django import forms 
from django.core.mail import send_mail
from django.template import RequestContext 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.context_processors import csrf
from forms import CcrForm, EditCcrForm, ReviewStatusForm, ApproveStatusForm
from ccrform.models import Ccr, Revision, STATUS_CHOICES, CcrFilter
from datetime import datetime
from ccrform.models import User, Revision, Notification
from templatetags.ccr_extras import has_group
import django_filters
from django.core.mail import send_mail


#REVIEWED_CCR_EMAIL = "The CCR "+ccr.ccr_number+" has been reviewed with the following comments: "+ccr.comments_r

#FOR_APPROVAL_EMAIL = "The CCR "+ccr.ccr_number+"  requires your approval. Follow the link to CCR site. http://52.49.166.20/ccrform/userprofile" 

#APPROVED_EMAIL = "The CCR " +ccr.ccr_number+ "has been approved with the following comments:" +ccr.comments_a+ " Please follow the link to complete the CCR http://52.49.166.20/ccrform/edit_ccr/"+ccr.ccr_number+"/"






# Create your views here.

@login_required 
def index(request):
	return HttpResponse("Welcome to the Index") 

@login_required
def view_ccr(request, ccr_number):
	ccr = get_object_or_404(Ccr, ccr_number=ccr_number)
	revs = Revision.objects.filter(ccr_ref = ccr)
	args = {}
	args['ccr'] = ccr
	args['revs'] = revs
	return render(request, 'ccrform/view_ccr.html', args)


	
@login_required
def create_ccr(request):
	if request.POST:
		form = CcrForm(request.POST)
		if form.is_valid():
			ccr = form.save(commit=False)
			NEW_CCR_EMAIL = "You have a new CCR for review. Follow the link to view your CCRs currently for review http://52.49.166.20/ccrform/userprofile/ "
			ccr.entered_by = request.user 
			send_mail('New CCR', NEW_CCR_EMAIL, 'support@vgtsi.com', [ccr.reviewer.email], fail_silently=False)  
			form.save()	
			ccr.ccr_number = str(ccr.date) +'-'+ str(ccr.id).zfill(4) 
			form.save()
			ccr_number = str(ccr.ccr_number) 
			notification = Notification(user=ccr.reviewer, ccr=ccr)
			notification.save()
			return HttpResponseRedirect('/ccrform/ccr/'+ccr_number+'/')
	else:
		form = CcrForm()
	args = {}
	args['form'] = form
	args.update(csrf(request))
	return render(request, 'ccrform/create_ccr.html', args)

		
@login_required
def change_status(request, ccr_number):
	ccr = get_object_or_404(Ccr, ccr_number=ccr_number)
	if has_group(request.user, "Approvers"):
		form = ApproveStatusForm(request.POST or None, instance=ccr)
		#email = approver email 
		new_notification_for = ccr.entered_by
	else:
		form = ReviewStatusForm(request.POST or None, instance=ccr)
		new_notification_for = ccr.approver
		#email = reviewer email 

		
	if request.POST: 
		if form.is_valid():
			ccr = form.save(commit=False)
			new_rev = Revision(edited_by=request.user, ccr_ref=ccr, status_at_rev=ccr.status, date=datetime.now())
			
			#send_mail() 
			form.save()
			new_rev.save()
			notification = get_object_or_404(Notification, ccr=ccr)
			if "Rejected" not in ccr.status:
				notification.user = new_notification_for
			else:
				notification.user = ccr.entered_by
			notification.seen = False
			notification.save()
			return HttpResponseRedirect('/ccrform/ccr/'+str(ccr.ccr_number)+'/')	
	args = {}
	args['form'] = form
	args.update(csrf(request))
	return render(request, 'ccrform/review_ccr.html', args)


@login_required
def edit_ccr(request, ccr_number):

	ccr = get_object_or_404(Ccr, ccr_number=ccr_number)
	if request.user == ccr.entered_by:
		form = EditCcrForm(request.POST or None, instance=ccr)
		args = {}
		args['ccr'] = ccr
		if request.POST:
			if form.is_valid():
				new_rev = Revision(edited_by=request.user, ccr_ref=ccr, status_at_rev=ccr.status, date=datetime.now())
				new_rev.save() 
				form.save()
				if ccr.status == "Complete" or "Rejected":
					notification = get_object_or_404(Notification, ccr=ccr)
					notification.seen = True
					notification.save()
				if ccr.status == "For Review":
					notification.user = ccr.reviewer
					notification.seen = False 
					notification.save()
				return HttpResponseRedirect('/ccrform/ccr/'+str(ccr.ccr_number)+'/')
 
		else:
			form = EditCcrForm(request.POST or None, instance=ccr)
		args['form'] = form 
		args.update(csrf(request))
		return render(request, 'ccrform/edit_ccr.html', args) 
	else:	
		return noaccess(request)


@login_required
def view_all_ccr(request):
	ccr_list = Ccr.objects.all()
	f = CcrFilter(request.GET, queryset=Ccr.objects.all())
	context = {}
	context['filtered'] = f
	context['ccr_list'] = ccr_list
	return render(request, 'ccrform/view_all_ccr.html', context)

@login_required
def user_profile(request):
	
	entered = Ccr.objects.filter(entered_by = request.user).order_by('-date')
	reviews = Ccr.objects.filter(reviewer = request.user, status="For Review").order_by('-date')
	approvals = Ccr.objects.filter(approver = request.user, status="For Approval").order_by('-date')
	context = {
			'entered': entered,
			'reviews': reviews,
			'approvals': approvals,
			
		}
	return render(request, 'ccrform/user_profile.html', context)

@login_required
def noaccess(request):
	return render(request, 'ccrform/noaccess.html')

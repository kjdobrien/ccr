from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Ccr(models.Model):

	OPEN 		= 'Open'
	FOR_REVIEW 	= 'For Review'
	FOR_APPROVAL	= 'For Approval'
	APPROVED	= 'Approved'
	COMPLETE	= 'Complete'

	STATUS_CHOICES = (
				
		(OPEN, 'Open'),
		(FOR_REVIEW, 'For Review'),
		(FOR_APPROVAl, 'For Approval'),
		(APPROVED, 'Approved'),
		(COMPLETE, 'Complete'),
			
			)
	
	VMWARE	= 'Vmware'
	WS2K8	= 'Windows Server 2008'
	WS2K12	= 'Windows Server 2012'
	F5_GTM	= 'F5 GTM'
	F5_LTM	= 'F5 LTM'
	CISCO_SWITCH = 'Cisco Switch'
	CHECKPOINT_FIREWALL = 'Checkpoint Firewall'
	CISCO_WIRELESS = 'Cisco Wireless'
	3_PAR_STORAGE = '3 Par Storage'
	HP_STORAGE = 'HP Storage'
	ISCSI_SWITCH = 'ISCSI Switch'
	TAPE_BACKUP = 'Tape Backup'
	ILO = 'ILO'
	BROCADE = 'Brocade'
	LINUX = 'Linux'
	AWS = 'AWS'
	APACHE = 'Apache'

	entered_by 		= models.ForeignKey(User)
	ccr_number 		= models.CharField(max_length=15)
	date			= models.DateField(auto_now = True)
	status			= models.Charfield(max_length=15,choices=STATUS_CHOICES,default=OPEN)
	reviewer	= models.ForeignKey(User)
	approver	= models.ForeignKey(User)
	technology_type = models.CharField(LIST)
	device_app	= models.ForeignKey(DeviceApp)
	name		= models.CharField(max_length=70)
	description	= models.TextField()
	date_of_change	= models.DateField(auto_now=False)
	reason		= models.TextField()
	roll_back_plan	= models.TextField()
	is_downtime	= models.BooleanField()
	time_to_change	= models.CharField(max_length=120)
	risk		= models.CharField(LIST)
	users_affected  = models.BooleanField()
	stnd_maintenance= models.BooleanField()
	implamenter	= models.ForeignKey(User)
	location	= models.CharField(LIST)
	date_of_review	= models.DateField(auto_now=False)
	date_approved	= models.DateField(auto_now=False)
	completed_by	= models.ForeignKey(User)
	completion_date	= models.DateField(auto_now=False)
	rev_number	= models.ForeignKey(Revision)




	



from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
#from managers import UsersManager

# Create your models here.

OPEN 		= 'Open'
FOR_REVIEW 	= 'For Review'
FOR_APPROVAL	= 'For Approval'
APPROVED	= 'Approved'
REJECTED	= 'Rejected'
COMPLETE	= 'Complete'

STATUS_CHOICES = (
				
		(OPEN, 'Open'),
		(FOR_REVIEW, 'For Review'),
		(FOR_APPROVAL, 'For Approval'),
		(APPROVED, 'Approved'),
		(REJECTED, 'Rejected'),
		(COMPLETE, 'Complete'),
)

class Ccr(models.Model):

	VMWARE		= 'Vmware'
	WS2K8		= 'Windows Server 2008'
	WS2K12		= 'Windows Server 2012'
	F5_GTM		= 'F5 GTM'
	F5_LTM		= 'F5 LTM'
	CISCO_SWITCH 	= 'Cisco Switch'
	FIREWALL 	= 'Checkpoint Firewall'
	CISCO_WIRELESS 	= 'Cisco Wireless'
	THREE_PAR_STORAGE 	= '3 Par Storage'
	HP_STORAGE 	= 'HP Storage'
	ISCSI_SWITCH 	= 'ISCSI Switch'
	TAPE_BACKUP	= 'Tape Backup'
	ILO 		= 'ILO'
	BROCADE 	= 'Brocade'
	LINUX 		= 'Linux'
	AWS 		= 'AWS'
	APACHE 		= 'Apache'
	ANTIVIRUS 	= 'Anti Virus'
	ESX 		= 'ESX Host'
	PHYSICAL_HOST 	= 'Physical Host'
	NIC 		= 'NIC'
	WSQLSERVER 	= 'Windows SQL Server'
	APPLICATION 	= 'Application'
	SFTP 		= 'SFTP Server Software'

	TECH_TYPE_CHOICES = (
		(VMWARE, 'Vmware'),
		(WS2K8, 'Windows Server 2008'),
		(WS2K12, 'Windows Server 2012'),
		(F5_GTM, 'F5 GTM'),
		(F5_LTM, 'F5 LTM'),
		(CISCO_SWITCH, 'Cisco Switch'),
		(FIREWALL, 'Checkpoint Firewall'),
		(CISCO_WIRELESS, 'Cisco Wireless'),
		(THREE_PAR_STORAGE, '3 Par Storage'),
		(HP_STORAGE, 'HP Storage'),
		(ISCSI_SWITCH, 'ISCSI Switch'),
		(TAPE_BACKUP, 'Tape Backup'),
		(ILO, 'ILO'),
		(BROCADE, 'Brocade'),
		(LINUX, 'Linux'),
		(AWS, 'AWS'),
		(APACHE, 'Apache'),
		(ANTIVIRUS, 'Anti Virus'),
		(ESX, 'ESX Host'),
		(PHYSICAL_HOST, 'Physical Host'),
		(NIC, 'NIC'),
		(WSQLSERVER, 'Windows SQL Server'),
		(APPLICATION, 'Application'),
		(SFTP, 'SFTP Server Software'),
	
)
	CORK = 'Cork'
	DUB  = 'Dublin' 

	LOCATION_CHOICES = (
	
	
	(CORK, 'Cork'),
	(DUB, 'Dublin'),
)

	DEVICE = 'Device'
	APP = 'Application'

	DEVICEAPP_CHOICES = (

	(DEVICE, 'Device'),
	(APP, 'Application'),

)

	LOW  = 'Low'
	MOD  = 'Moderate'
	HIGH = 'High'

	RISK_CHOICES = (

		(LOW, 'Low'),
		(MOD, 'Moderate'),
		(HIGH, 'High'),
)

	entered_by 	= models.ForeignKey(User, related_name='creator')
	ccr_number 	= models.CharField(max_length=15)
	date		= models.DateField(auto_now = True)
	status		= models.CharField(max_length=15,choices=STATUS_CHOICES,default=OPEN)
	reviewer	= models.ForeignKey(User, related_name='nominated_reviewer')
	approver	= models.ForeignKey(User, related_name='nominated_approver')
	technology_type = models.CharField(max_length=20, choices=TECH_TYPE_CHOICES)
  	device_app	= models.CharField(max_length=15, choices=DEVICEAPP_CHOICES)
	name		= models.CharField(max_length=70)
	description	= models.TextField()
	date_of_change	= models.DateField(auto_now=False)
	reason		= models.TextField()
	roll_back_plan	= models.TextField()
	is_downtime	= models.BooleanField(default=False)
	downtime_duration = models.CharField(max_length=120)
	time_to_change	= models.CharField(max_length=120)
	risk		= models.CharField(max_length=4, choices=RISK_CHOICES)
	users_affected  = models.BooleanField(default=False)
	maintenance	= models.BooleanField(default=False)
	implamenter	= models.ForeignKey(User, related_name='change_implamenter')
	location	= models.CharField(max_length=6, choices=LOCATION_CHOICES)
	date_of_review	= models.DateField(auto_now=False, null=True)
	comments_r	= models.TextField(null=True)
	date_approved	= models.DateField(auto_now=False, null=True)
	comments_a	= models.TextField(null=True)
	completed_by	= models.ForeignKey(User, null=True, related_name='completer')
	completion_date	= models.DateField(auto_now=False, null=True) 
	



class Revision(models.Model):
	edited_by 	= models.ForeignKey(User)
	ccr_ref		= models.ForeignKey(Ccr) 
	status_at_rev	= models.CharField(max_length=15,choices=STATUS_CHOICES,default=OPEN)
	date 		= models.DateField(auto_now=False) 

	


from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models import Q 
import django_filters
from django_filters import ChoiceFilter, CharFilter
#from managers import UsersManager

# Create your models here.

OPEN 		= 'Open'
FOR_REVIEW 	= 'For Review'
FOR_APPROVAL	= 'For Approval'
APPROVED	= 'Approved'
REJECTED	= 'Rejected'
REJECTED_AMEND 	= 'Rejected for Amendments'
COMPLETE	= 'Complete'

STATUS_CHOICES = (
				
		(OPEN, 'Open'),
		(FOR_REVIEW, 'For Review'),
		(FOR_APPROVAL, 'For Approval'),
		(APPROVED, 'Approved'),
		(REJECTED, 'Rejected'),
		(REJECTED_AMEND, 'Rejected for Amendments'),
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

	def limit_to_reviewers():
		users = User.objects.filter(groups='Reviewers')
		return users


	

	entered_by 	= models.ForeignKey(User, related_name='creator')
	ccr_number 	= models.CharField(max_length=15)
	date		= models.DateField(auto_now = True)
	status		= models.CharField(max_length=23,choices=STATUS_CHOICES,default=OPEN)
	reviewer	= models.ForeignKey(User, related_name='nominated_reviewer', limit_choices_to = {'groups':2})
	approver	= models.ForeignKey(User, related_name='nominated_approver', limit_choices_to = {'groups':1})
	technology_type = models.CharField(max_length=20, choices=TECH_TYPE_CHOICES)
  	device_app	= models.CharField(max_length=15, choices=DEVICEAPP_CHOICES, verbose_name="Device or Application", blank=True)
	name		= models.CharField(max_length=70)
	description	= models.TextField()
	date_of_change	= models.DateField(auto_now=False)
	reason		= models.TextField()
	roll_back_plan	= models.TextField()
	is_downtime	= models.BooleanField(default=False, verbose_name="Is there Downtime")
	downtime_duration = models.CharField(max_length=120, null=True)
	time_to_change	= models.CharField(max_length=120)
	risk		= models.CharField(max_length=8, choices=RISK_CHOICES, null=True)
	users_affected  = models.BooleanField(default=False, verbose_name="Are Users Affected?")
	maintenance	= models.BooleanField(default=False, verbose_name="Is this Standard Maintenance")
	implamenter	= models.ForeignKey(User, related_name='change_implamenter')
	location	= models.CharField(max_length=6, choices=LOCATION_CHOICES)
	date_of_review	= models.DateField(auto_now=False, null=True)
	comments_r	= models.TextField(null=True, verbose_name="Comments")
	date_approved	= models.DateField(auto_now=False, null=True)
	comments_a	= models.TextField(null=True, verbose_name="Comments")
	completed_by	= models.ForeignKey(User, null=True, related_name='completer', blank=True)
	completion_date	= models.DateField(auto_now=False, null=True, blank=True) 
	



class Revision(models.Model):
	edited_by 	= models.ForeignKey(User)
	ccr_ref		= models.ForeignKey(Ccr) 
	status_at_rev	= models.CharField(max_length=15,choices=STATUS_CHOICES,default=OPEN)
	date 		= models.DateField(auto_now=False) 

class Notification(models.Model):
	user 	= models.ForeignKey(User)
	ccr	= models.ForeignKey(Ccr)
	seen 	= models.BooleanField(default=False)
	date	= models.DateField(auto_now=True)


class CcrFilter(django_filters.FilterSet):

	def __init__(self, *args, **kwargs):
		super(CcrFilter, self).__init__(*args, **kwargs)

		for name, field in self.filters.iteritems():
			if isinstance(field, ChoiceFilter):
				field.extra['choices'] = tuple([("","Any"),]+ list(field.extra['choices']))

	name = django_filters.CharFilter(lookup_type='icontains')

	class Meta:
		model = Ccr
		fields = ['technology_type', 'status', 'device_app', 'name', 'risk', 'location']


from django import forms
from models import Ccr, Revision 


class CcrForm(forms.ModelForm):
	class Meta:
		model = Ccr
		widgets = {'date_of_change : forms.SelectDateWidget'}
		fields = ['reviewer', 'approver', 'technology_type', 'device_app', 'name', 'description', 'date_of_change', 'reason', 'roll_back_plan', 'is_downtime', 'downtime_duration', 'time_to_change', 'risk', 'users_affected', 'maintenance', 'implamenter', 'location']

class ReviewStatusForm(forms.ModelForm):
	class Meta:
		model = Ccr
		fields = ['date_of_review', 'comments_r']

class ApproveStatusForm(forms.ModelForm):
	class Meta:
		model = Ccr
		fields = ['date_approved', 'comments_a']

class EditCcrForm(forms.ModelForm):
	class Meta: 
		model = Ccr
		exclude = ('entered_by', 'ccr_number', 'date_of_review', 'comments_r', 'date_approved', 'comments_a',)


		


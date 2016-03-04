from django import forms
from models import Ccr, Revision, STATUS_CHOICES 


class CcrForm(forms.ModelForm):
	class Meta:
		model = Ccr
		widgets = {
		'date_of_change' : forms.SelectDateWidget,
		'is_downtime' : forms.CheckboxInput(attrs={'switch':'is_downtime'}),
		}
		fields = ['reviewer', 'approver', 'technology_type', 'device_app', 'name', 'description', 'date_of_change', 'reason', 'roll_back_plan', 'is_downtime', 'downtime_duration', 'time_to_change', 'risk', 'users_affected', 'maintenance', 'implamenter', 'location']

class ReviewStatusForm(forms.ModelForm):
	class Meta:
		model = Ccr
		fields = ['status', 'date_of_review', 'comments_r']

	def __init__(self, *args, **kwargs):
		super(ReviewStatusForm, self).__init__(*args, **kwargs)
		limit_choices = [STATUS_CHOICES[2], STATUS_CHOICES[4], STATUS_CHOICES[5]]
		self.fields['status'].choices = limit_choices
			

class ApproveStatusForm(forms.ModelForm):
	class Meta:
		model = Ccr
		fields = ['status','date_approved', 'comments_a']
		
	def __init__(self, *args, **kwargs):
		super(ApproveStatusForm, self).__init__(*args, **kwargs)
		limit_choices = [STATUS_CHOICES[3], STATUS_CHOICES[4], STATUS_CHOICES[5]]
		self.fields['status'].choices = limit_choices

class EditCcrForm(forms.ModelForm):
	class Meta: 
		model = Ccr
		exclude = ('entered_by', 'ccr_number', 'date_of_review', 'comments_r', 'date_approved', 'comments_a',)


		


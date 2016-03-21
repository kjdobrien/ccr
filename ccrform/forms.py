from django import forms
from models import Ccr, Revision, STATUS_CHOICES 


class CcrForm(forms.ModelForm):
	class Meta:
		model = Ccr
		widgets = {

		'date_of_change' : forms.DateInput(attrs={'id' : 'datepicker'}),
		'is_downtime' : forms.CheckboxInput(attrs={'switch':'is_downtime'}),
		}
		date_of_change = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
		fields = ['reviewer', 'approver', 'technology_type', 'device_app', 'name', 'description', 'date_of_change', 'reason', 'roll_back_plan', 'is_downtime', 'downtime_duration', 'time_to_change', 'risk', 'users_affected', 'maintenance', 'implamenter', 'location']
	
class ReviewStatusForm(forms.ModelForm):
	class Meta:
		model = Ccr
		widgets = {'date_of_review' : forms.DateInput(attrs={'id' : 'datepicker'}),}	
		fields = ['status', 'date_of_review', 'comments_r']

	def __init__(self, *args, **kwargs):
		super(ReviewStatusForm, self).__init__(*args, **kwargs)
		limit_choices = [STATUS_CHOICES[2], STATUS_CHOICES[4], STATUS_CHOICES[5]]
		self.fields['status'].choices = limit_choices
			

class ApproveStatusForm(forms.ModelForm):
	class Meta:
		model = Ccr
		widgets = {'date_approved' : forms.DateInput(attrs={'id' : 'datepicker'}),}	
		fields = ['status','date_approved', 'comments_a']
		
	def __init__(self, *args, **kwargs):
		super(ApproveStatusForm, self).__init__(*args, **kwargs)
		limit_choices = [STATUS_CHOICES[3], STATUS_CHOICES[4], STATUS_CHOICES[5]]
		self.fields['status'].choices = limit_choices

class EditCcrForm(forms.ModelForm):
	class Meta: 
		model = Ccr
		widgets = {
			#'date_of_change' : forms.DateInput(attrs={'id': 'datepicker'}),
			'completion_date': forms.DateInput(attrs={'id': 'datepicker'}),
		
		}
		exclude = ('entered_by', 'ccr_number', 'date_of_review', 'comments_r', 'date_approved', 'comments_a',)


		


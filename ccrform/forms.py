from django import forms
from models import Ccr, Revision 


class CcrForm(forms.ModelForm):
	class Meta:
		model = Ccr
		fields = ['reviewer', 'approver', 'technology_type', 'device_app', 'name', 'description', 'date_of_change', 'reason', 'roll_back_plan', 'is_downtime', 'downtime_duration', 'time_to_change', 'risk', 'users_affected', 'maintenance', 'implamenter', 'location']

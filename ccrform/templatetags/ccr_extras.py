from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
@stringfilter
def remove_special(value):
	nosp = ''.join(e for e in value if e.isalnum())
	return nosp 

@register.filter
def has_group(user, group_name):
	group = Group.objects.get(name=group_name)
	return True if group in user.groups.all() else False

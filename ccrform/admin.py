from django.contrib import admin
from .models import User, Ccr, Revision, Notification
# Register your models here.


class CcrAdmin(admin.ModelAdmin):
	list_display = ('name', 'date', 'entered_by')

class RevisionAdmin(admin.ModelAdmin):
	list_display = ('ccr_ref.name', 'date', 'edited_by',)



admin.site.register(Ccr)
admin.site.register(Revision)
admin.site.register(Notification)



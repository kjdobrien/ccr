
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^create_ccr/$', views.create_ccr, name='create_ccr' ),
	url(r'^view_all_ccr/$', views.view_all_ccr, name='view_all_ccr'),
	url(r'^ccr/(?P<ccr_number>(.*))/$', views.view_ccr, name='view_ccr'),
	url(r'^edit_ccr/(?P<ccr_number>(.*))/$', views.edit_ccr, name='edit_ccr'),
	url(r'^review_ccr/(?P<ccr_number>(.*))/$', views.change_status, name='change_status'),
	url(r'^user_profile/$', views.user_profile, name='user_profile'),
]


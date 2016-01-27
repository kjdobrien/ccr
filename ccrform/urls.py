
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^ccr/create/$', views.create_ccr, name='create_ccr' ),
	
]


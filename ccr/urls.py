"""ccr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import ccr.views 

urlpatterns = [
    	url(r'^ccrform/', include('ccrform.urls', namespace = "ccrform")),
	url(r'^admin/', admin.site.urls),

	#url(r'^$', ccr.views.home),

	url(r'^$', ccr.views.login_view),
	url(r'^accounts/auth_view/$', ccr.views.auth_view),
	url(r'^accounts/logout/$', ccr.views.logout_view),
	url(r'^accounts/loggedin/$', ccr.views.loggedin),
	url(r'^accounts/invalid/$', ccr.views.invalid_login), 
]

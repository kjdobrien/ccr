"""
WSGI config for ccr project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
import site 
#Add the site-packages of the chosen virtual env to work with 
site.addsitedir('/home/ubuntu/ccr-env/lib/python2.7/site-packages')

#Add the app's directory to the PYTHONPATH
sys.path.append('/home/ubuntu/ccr')
sys.path.append('/home/ubuntu/ccr/ccr')
os.environ["DJANGO_SETTINGS_MODULE"] = 'ccr.settings'

#Activate your virtual env 
activate_env=os.path.expanduser("/home/ubuntu/ccr-env/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.wsgi
application = django.core.wsgi.get_wsgi_application()

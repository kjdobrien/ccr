from django.db import models

class UsersManager(models.Manager):
	def for_user(self, user):
		return super(UsersManager, self).get_query_set().filter(user=user)

class UserMan(models.Model):
	objects = UsersManager() 

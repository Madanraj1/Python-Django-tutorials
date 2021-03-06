from django.db import models

from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager
	)

class UserManager(BaseUserManager):
	def create_user(self, email, password=None):

		if not email:
			raise ValueError('user must have an email address')

		user = self.model( email=self.normalize_email(email),)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_staffuser(self,email, password):

		user = self.create_user(
			email,
			password = password,
			)
		user.staff = True
		user.save(using=self._db)
		return user

	def create_superuser(self,email, password):

		user = self.create_user(
			email,
			password = password,
			)
		user.staff = True
		user.admin = True
		user.save(using=self._db)
		return user





class User(AbstractBaseUser):
	email 	= models.EmailField( max_length=255, unique=True) 
	active	= models.BooleanField(default=True)
	staff   = models.BooleanField(default=False)  #admin user  non-superuser
	admin   = models.BooleanField(default=False) # superuser
	#password

	USERNAME_FIELD = 'email'
	REQUIRED_FIELD = [] # email & password are required by default

	objects = UserManager()

	def get_full_name(self):
		return self.email 

	def get_short_name(self):
		return self.email 

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True 

	def has_module_perms(self, app_label):
		return True 


	@property 
	def is_staff(self):
		return self.staff 

	@property 
	def is_admin(self):
		return self.admin 

	@property 
	def is_active(self):
		return self.active 
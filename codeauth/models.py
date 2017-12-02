from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomeUserManager(BaseUserManager):
	# the common opreation
	def _create_user(self, email, phone, password, is_staff, **extra_fields):
		if not email:
			raise ValueError('Users must have an email address')
		email = self.normalize_email(email)
		user = self.model(email=email, 
			phone=phone,
			# is_active=False,
			is_active=True,
			is_staff=is_staff)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, phone, password=None, **other_fields):
		return self._create_user(email, phone, password, False, **other_fields)

	def create_superuser(self, email, phone, password, **other_fields):
		return self._create_user(email, phone, password, True, **other_fields)

		
class User(AbstractBaseUser):
	MANAGER, TEACHER, STUDENT = range(3)
	CHARACTER = (
		(MANAGER, 'Project manager'),
		(TEACHER, 'Teacher'),
		(STUDENT, 'Student')
	)
	is_staff = models.BooleanField(
		default=False,
	)
	email = models.EmailField( 
		unique=True
	)
	phone = models.BigIntegerField(
		unique=True
	)
	password = models.CharField(
		max_length=128
	)
	is_active = models.BooleanField(
		default=False
	)
	user_type = models.PositiveSmallIntegerField(
		choices=CHARACTER,
		default=STUDENT
	)
	introduction = models.TextField()
	experience = models.CharField(
		max_length=2048
	)
	date_joined = models.DateTimeField(
		auto_now_add=True
	)
	date_updated = models.DateTimeField(
		auto_now=True
	)
	# used as the unique identifier.
	USERNAME_FIELD = 'email'
	'''
	A list of the field names that will be prompted for 
	when creating a user via the createsuperuser management command. 
	'''
	REQUIRED_FIELDS = ['phone']
	objects = CustomeUserManager()

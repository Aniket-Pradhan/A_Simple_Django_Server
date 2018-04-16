from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

class CustomUserManager(UserManager):
	pass

class CustomUser(AbstractUser):
	username = models.CharField(('username'), max_length=30, unique=True) 
	first_name = models.CharField(('first name'), max_length=30, blank=True)
	last_name = models.CharField(('last name'), max_length=30, blank=True)
	email = models.EmailField(('email address'), blank=True)
	bio = models.CharField(('bio'), max_length=100, blank=True)


class Upload(models.Model):
	pic = models.FileField(upload_to="images/")    
	upload_date=models.DateTimeField(auto_now_add =True)

class UploadForm(ModelForm):
	class Meta:
		model = Upload
		fields = ('pic',)

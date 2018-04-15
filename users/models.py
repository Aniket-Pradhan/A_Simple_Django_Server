from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()


class Upload(models.Model):
    pic = models.FileField(upload_to="images/")    
    upload_date=models.DateTimeField(auto_now_add =True)

class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('pic',)
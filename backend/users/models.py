from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, unique=False, null=False)
    email = models.EmailField(max_length=20, null=True, blank=True, unique=False)
    mobileNumber = PhoneNumberField(unique=False, null=False)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.profile.name + 'doctor'
class Owner(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.profile.name + 'owner'
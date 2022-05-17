from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=60, unique=False)
    PESEL = models.TextField(max_length=11, validators=[MinLengthValidator(11)], unique=False, null=True, blank=True)
    email = models.EmailField(max_length=20, null=True, blank=True, unique=False)
    mobileNumber = PhoneNumberField(unique=False, null=True, blank=True)

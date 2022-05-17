from django.db import models

# Create your models here.

class Profile(models.Model):
    email = models.EmailField(max_length=20, null=True, blank=True)
from django.contrib import admin
from . models import Profile, Doctor, Owner
# Register your models here.
admin.site.register(Profile)
admin.site.register(Owner)
admin.site.register(Doctor)
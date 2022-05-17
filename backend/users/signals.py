from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from django.dispatch import receiver
from . models import Profile, Owner


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Profile)
def create_profile_owner(sender, instance, created, **kwargs):
    if created:
        Owner.objects.create(profile=instance)

@receiver(post_save, sender=Profile)
def save_profile_owner(sender, instance, **kwargs):
    instance.owner.save()
    
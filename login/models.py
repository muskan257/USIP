

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    
   
    phone = models.CharField(max_length=20, blank=True, default='')
    
    email = models.CharField(max_length=100, default='', blank=True)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

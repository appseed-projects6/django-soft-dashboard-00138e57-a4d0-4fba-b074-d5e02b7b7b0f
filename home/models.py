# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Games(models.Model):

    #__Games_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    link_steam = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    file_name = models.CharField(max_length=255, null=True, blank=True)
    file_path = models.CharField(max_length=255, null=True, blank=True)
    command = models.CharField(max_length=255, null=True, blank=True)

    #__Games_FIELDS__END

    class Meta:
        verbose_name        = _("Games")
        verbose_name_plural = _("Games")



#__MODELS__END

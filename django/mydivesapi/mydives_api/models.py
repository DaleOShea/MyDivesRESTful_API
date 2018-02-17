from django.db import models
from django.contrib.auth.models import AbstrachBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


name = models.CharField(max_length = 250);
email = models.CharField(max_length = 250, unique=True);
is_staff = models.BooleanField(default = False);
is_active = models.BooleanField(default = True)

USERNAME_FIELD = 'email';
REQUIRED_FIELDS = ['name'];


def get_full_name(self):
    return self.email

def get_short_name
    return self.name

def __str__(self):
    return self.email

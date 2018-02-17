from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length = 250)
    email = models.CharField(max_length = 250, unique=True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

class UserManager(BaseUserManager):
    def create_user(self, name, email, password = None):

        if not email:
            raise ValueError('Please enter an email address')

        user = self.model(
               email = self.normalize_email(email),
               name = name
               )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, name, email, password):

        user = self.create_user(name, email, password = password)

        user.is_admin = True
        user.save(using = self._db)

        return user

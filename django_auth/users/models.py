from django.db import models, transaction

# users/models.py 
#from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """ 
Creates and saves a User with the given email,and password.
""" 
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save()
                return user
        except:
            raise
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """ 
An abstract base class implementing a fully featured User model with 
admin-compliant permissions. 

"""
    email = models.EmailField(max_length=40, unique=True)
    can_be_contacted  = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["can_be_contacted", "can_data_be_shared", "age"]    
    def save(self, *args, **kwargs):
        if self.age<15:
            self.can_data_be_shared = False
        super(User, self).save(*args, **kwargs)
        return self

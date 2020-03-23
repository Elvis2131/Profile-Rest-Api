from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):

    def create_user(self,email,name,password=None):
        """How to create a new user profile object
        """
        if not email:
            raise ValueError('User must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db)

        return user

    
    def create_superuser(self, email, password):
        """Creates and saves an new super user"""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile in the system
    """
    email = models.EmailField(unique = True, max_length=254)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get the users full name
        """
        return self.name

    def get_short_name(self):
        """Getting the users short name"""
        return self.name

    def __str__(self):
        return self.email
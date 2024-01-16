from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address') # raise ValueError is required for BaseUserManager
        email = self.normalize_email(email) # normalize_email is required for BaseUserManager
        user = self.model(email=email, name=name) # self.model is required for BaseUserManager
        user.set_password(password) # set_password is required for BaseUserManager
        user.save(using=self._db) # using=self._db is required for BaseUserManager
        
        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password) # create_user is required for BaseUserManager
        user.is_superuser = True # is_superuser is required for PermissionsMixin
        user.is_staff = True # is_staff is required for PermissionsMixin
        user.save(using=self._db) # using=self._db is required for BaseUserManager
        
        return user
    

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True) # max_length is required for CharField
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # is_active is required for PermissionsMixin
    is_staff = models.BooleanField(default=False) # is_staff is required for PermissionsMixin

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' # USERNAME_FIELD is required for AbstractBaseUser
    REQUIRED_FIELDS = ['name'] # REQUIRED_FIELDS is required for AbstractBaseUser

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    def __str__(self):
        """Return string representation of user"""
        return self.email
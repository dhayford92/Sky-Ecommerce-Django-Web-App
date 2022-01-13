from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **kwargs):
        email = self.normalize_email(email)
        now = timezone.now()
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,
            date_joined = now
            **kwargs
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, password=None, **kwargs):
        return self._create_user(email, password, False, False, **kwargs)
    
    def create_superuser(self, email, password, **kwargs):
        user = self._create_user(email, password, True, True, **kwargs)
        user.save(using=self._db)
        return user
    


class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(blank=True, null=True, max_length=250)
    email = models.EmailField(unique=True)
    phone_number= models.CharField(blank=True, null=True, max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        if self.fullname is None:
            return self.email
        else:
            return self.fullname
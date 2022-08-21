from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("email is required")
        if not password:
            raise ValueError("password is required")
        nor_email = self.normalize_email(email)
        user = self.model(email=nor_email,**extra_fields)
        user.set_password(password)
        return user.save()
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        self.create_user(email,password,**extra_fields)



class CustomUser(AbstractUser):
    email = models.EmailField(null=False,blank=False,max_length=300,unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username


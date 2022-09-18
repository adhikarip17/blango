from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

class BlangoUserManager(UserManager):
  def _create_user(self, email, password, **extra_fields):
    if not email:
      raise ValueError("Email must be Set")
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password=None, **extra_fields):
    extra_fields.setdefault("is_staff", False)
    extra_fields.setdefault("is_superuser",False)
    return self._create_user(email, password, **extra_fields)
  
  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault("is_staff",True)
    extra_fields.setdefault("is_superuser",True)

    if extra_fields.get("is_staff") is not True:
      raise ValueError("Superuser must have is_staff=T")




class User(AbstractUser):
  pass
  
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    experience = models.TextField()
    skills = models.TextField()
    position = models.CharField(max_length=255)
    salary_expectation = models.IntegerField()
    about = models.TextField()
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    salary_expectation = models.IntegerField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

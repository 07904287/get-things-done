from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    number_of_cookies = models.IntegerField(default=0)

class Tasks(models.Model):
    ACTIVE = 'Active'
    SNOOZED = 'Snoozed'
    COMPLETED = 'Completed'
    CANCELED = 'Canceled'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (SNOOZED, 'Snoozed'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
    ]
    content = models.CharField(max_length=180)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="poster")
    deadline = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    attachment = models.FileField(null=True, blank=True)
    percentage_done = models.IntegerField(default=0)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=ACTIVE)
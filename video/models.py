from pyexpat import model
from statistics import mode
from turtle import title
from django.db import models
from django.contrib.auth.models import User

class VideoPlan(models.Model):
    title = models.CharField(max_length=255)
    desctiption = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    premium = models.BooleanField(default=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripeid = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DailyLog(models.Model):
    checkin_time = models.DateTimeField(auto_now_add=True, max_length=100, null=False)
    checkin_message = models.CharField(max_length=500, null=True, blank=True)
    checkout_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    checkout_message = models.CharField(max_length=500, null=True, blank=True)
    status = models.IntegerField(max_length=10, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

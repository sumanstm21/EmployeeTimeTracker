from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.utils.translation import ugettext_lazy as _

# Create your models here.
class DailyLog(models.Model):
    checkin_time = models.DateTimeField(default=datetime.now, null=True, blank=True)
    checkin_message = models.CharField(max_length=500, null=True, blank=True)
    checkout_time = models.DateTimeField(default=datetime.now, blank=True)
    checkout_message = models.CharField(max_length=500, null=True, blank=True)
    status = models.IntegerField(blank=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Daily Log')
        verbose_name_plural = _('Daily Logs')

    def __str__(self):
        return str('%s %s' % (self.checkin_time, self.user))

class BreakTime(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    time_period = models.TimeField(blank=False, null=False)

    def __str__(self):
        return str('%s %s' % (self.time_period, self.name))
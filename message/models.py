from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

# Create your models here.
class message(models.Model):
    message = models.CharField(help_text=_('message'), max_length=600)
    date_created = models.DateTimeField(help_text=_('Date Created'), auto_now_add=True, null=True)
    user = models.ForeignKey(User, help_text=_('User'), on_delete=models.CASCADE)
    acknowledge = models.CharField(help_text=_('Acknowledge'), max_length=600, null=True, blank=True)

    def __str__(self):
        return self.message
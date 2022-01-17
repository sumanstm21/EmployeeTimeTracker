from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

# Create your models here.
gender_choice = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, help_text=_('User'), on_delete=models.CASCADE, null=True)
    first_name = models.CharField(help_text=_('first name'), max_length=200, null=True, blank=True)
    last_name = models.CharField(help_text=_('last name'), max_length=200, null=True, blank=True)
    email = models.CharField(help_text=_('Email'), max_length=200, null=True, blank=True)
    phone = models.CharField(help_text=_('Phone'), max_length=200, null=True, blank=True)
    gender = models.CharField(help_text=_('Gender'), max_length=10, choices=gender_choice, null=True, blank=True)
    address = models.CharField(help_text=_('Address'), max_length=200, null=True, blank=True)
    bank_name = models.CharField(help_text=_('Bank name'), max_length=200, null=True, blank=True)
    bank_account = models.CharField(help_text=_('Bank account'), max_length=200, null=True, blank=True)
    rate_per_hour = models.FloatField(help_text=_('Rate Per Hour'), null=True, blank=True)
    monthly_salary = models.FloatField(help_text=_('Monthly Salary'), null=True, blank=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profile')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

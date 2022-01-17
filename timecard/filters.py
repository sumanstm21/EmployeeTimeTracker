import django_filters
from django_filters import DateFilter
from .models import *
from django import forms

from django.utils.translation import ugettext_lazy as _


class DateInput(forms.DateInput):
    input_type = 'date'

class ReportFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="checkin_time", lookup_expr='from', localize=True)
    end_date = DateFilter(field_name="checkin_time", lookup_expr='to', localize=True, widget=DateInput())

    class Meta:
        model = DailyLog
        fields = '__all__'
        exclude = ['checkin_time', 'checkout_time', 'checkin_message', 'checkout_message', 'status']

from rest_framework import serializers
from .models import DailyLog

class dailylogSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyLog
        fields = '__all__'
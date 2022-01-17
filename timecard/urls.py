from django.urls import path
from . import views

urlpatterns = [
    path('', views.timecard, name='checkin'),
    path('record/', views.record, name='record'),
    path('allrecord/', views.allrecord, name='allrecord'),
    path('report/', views.report, name='report'),
    path('getreport/', views.getreport, name='getreport'),
    path('api/', views.DailyLogs.as_view(), name='getreport'),
]

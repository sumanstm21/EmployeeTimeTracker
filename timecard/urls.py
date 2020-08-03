from django.urls import path
from . import views

urlpatterns = [
    path('', views.timecard, name='checkin'),
    path('record/', views.record, name='record'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='video'),
    path('join/', views.join, name='join'),
    path('plan/', views.plan, name='plan'),
    path('checkout/', views.checkout, name='checkout'),
    # path('getreport/', views.getreport, name='getreport'),
    # path('api/', views.DailyLogs.as_view(), name='getreport'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='video'),
    path('join/', views.join, name='join'),
    path('plan/<int:pk>', views.plan, name='plan'),
    path('checkout/', views.checkout, name='checkout'),
    path('settings/', views.settings, name='settings'),
]

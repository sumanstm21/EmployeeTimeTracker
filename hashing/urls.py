from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hashing'),
    path('hash/<str:hash>', views.hash, name='hash'),
]

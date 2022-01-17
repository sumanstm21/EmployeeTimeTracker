from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='chatapp'),
    path('<str:room_name>/', views.room, name='room'),
]
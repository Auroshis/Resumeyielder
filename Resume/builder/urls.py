from django.urls import path, include
from . import views

urlpatterns = [
    path('resumepage/', views.resumepage),
    path('', views.index),
]
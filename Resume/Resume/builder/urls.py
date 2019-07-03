from django.urls import path, include
from . import views
#from .views import GeneratePdf
urlpatterns = [
    path('resumepage/', views.resumepage),
    #path('pdf/', GeneratePdf.as_view()),
    path('', views.index),
]
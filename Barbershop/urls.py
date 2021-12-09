
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax-posting/', views.ajax_posting, name='ajax_posting'), 
]

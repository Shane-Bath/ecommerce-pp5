from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_form, name='contact_form'),
]
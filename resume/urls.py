from django.contrib import admin
from django.urls import path
from .views import extract_resume

urlpatterns = [
    path('api/extract_resume/', extract_resume, name='extract-resume'),
]

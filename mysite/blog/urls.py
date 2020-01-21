from django.contrib import admin
from django.urls import path, re_path, include
from blog import views

urlpatterns = [
    path('new/story', views.story)
]
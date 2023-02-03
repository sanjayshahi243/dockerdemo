from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_files, name="list_file"),
    path("raise401/", views.raise_401, name="raise_401"),
    path("raise500/", views.raise_500, name="raise_500"),
    path("add/", views.add_files, name="add_file"),
]

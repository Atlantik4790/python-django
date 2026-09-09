"""URL routing: maps each path to one of the 3 views."""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("health", views.health, name="health"),
    path("api/items", views.items, name="items"),
]

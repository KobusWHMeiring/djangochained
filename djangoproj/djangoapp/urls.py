from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("<int:conversation_id>/", views.specific, name = "specific")
]

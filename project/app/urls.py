from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:name>/', views.home, name="home")
]
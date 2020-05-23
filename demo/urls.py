from django.urls import path
from . import views
from rest_framework import routers

#  crate a new variable called router
router = routers.DefaultRouter()

urlpatterns = [
    path('first', views.first),
]

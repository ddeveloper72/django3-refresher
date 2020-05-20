from django.urls import path
from . import views

urlpatterns = [
    path('firstfunction', views.first),
]

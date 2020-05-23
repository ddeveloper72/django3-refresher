from django.urls import path
from . import views
from rest_framework import routers

#  crate a new variable called router
router = routers.DefaultRouter()
# crate router called books & pass the viewset from the views
router.register('books', BookViewSet)

urlpatterns = [
    path('first', views.first),
]

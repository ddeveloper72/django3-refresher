from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet

#  crate a new variable called router
router = routers.DefaultRouter()
# crate router called books & pass the viewset from the views
router.register('books', BookViewSet)

# include the registered router into the url path
urlpatterns = [
    path('', include(router.urls)),
]

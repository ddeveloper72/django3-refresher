from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication

# Create your views here.


# crate a builtin view using viewsets
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer  # from class defined in serializer.py
    queryset = Book.objects.all()
    authentication_classes =()
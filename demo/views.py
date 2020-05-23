from rest_framework import viewsets
from .serializers import BookSerializer

# Create your views here.


# crate a builtin view using viewsets
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer  # from class defined in serializer.py
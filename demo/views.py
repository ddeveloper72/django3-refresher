from rest_framework import viewsets
from .serializers import BookSerializer, MiniBookSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.


# crate a builtin view using viewsets
class BookViewSet(viewsets.ModelViewSet):
    # devault view set uses MiniBookSerializer to only send a small amount of data 
    # from each book to the front end; such as id & title. This optimizes the app.
    serializer_class = MiniBookSerializer  # from class defined in serializer.py
    queryset = Book.objects.all()
    #  insure the TokenAuthentication is treated as a tuple by
    # adding a comma
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # the specific book serializer uses the full BookSerializer to retrieve all
    # data for a specific book; so optimizing the data being sent to frontend.
    # using a custom RetrieveModelMixin view function from mixins.py
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)

from rest_framework import serializers
from .models import Book, BookNumber


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # specify the fields available from serializer
        fields = ['id', 'isbn_10', 'isbn_13',]


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    class Meta:
        model = Book
        # specify the fields available from serializer
        fields = ['id', 'title', 'description', 'price', 'published', 'is_published', 'number']

from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # specify the fields available from serializer
        fields = ['id', 'title', 'description', 'price', 'published', 'is_published']

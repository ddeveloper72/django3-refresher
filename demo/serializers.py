from rest_framework import serializers
from .models import Book, BookNumber, Character


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        # specify the fields available from serializer
        fields = ['id', 'isbn_10', 'isbn_13']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        # specify the fields available from serializer
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)
    class Meta:
        model = Book
        # specify the fields available from serializer
        fields = ['id', 'title', 'description', 'price', 'published', 'is_published', 'number', 'characters']

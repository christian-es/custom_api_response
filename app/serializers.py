from rest_framework import serializers

from app.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = []

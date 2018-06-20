from rest_framework.viewsets import ModelViewSet

from app.models import Author, Book
from app.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    def get_queryset(self):
        return Author.objects.all()

    def get_serializer_class(self):
        return AuthorSerializer


class BookViewSet(ModelViewSet):
    def get_queryset(self):
        return Book.objects.all()

    def get_serializer_class(self):
        return BookSerializer

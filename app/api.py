from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

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

    def list(self, request, *args, **kwargs):

        book_list = Book.objects.all()

        json_response_list = []

        for book in book_list:
            author_book = {
                "name": book.author.name,
                "alias": book.author.alias
            }

            data = {
                "title": book.title,
                "pages": book.pages,
                "author": author_book
            }

            json_response_list.append(data)

        return Response(json_response_list)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        author_book = {
            "name": serializer.instance.author.name,
            "alias": serializer.instance.author.alias
        }

        data = {
            "title": serializer.instance.title,
            "pages": serializer.instance.pages,
            "author": author_book
        }

        return Response(data)

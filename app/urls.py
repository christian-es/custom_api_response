from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from app.api import AuthorViewSet, BookViewSet

VERSION_API = 'v1/'

router_author = DefaultRouter()
router_author.register(VERSION_API + 'author', AuthorViewSet, base_name='api_author_')

router_book = DefaultRouter()
router_book.register(VERSION_API + 'book', BookViewSet, base_name='api_book_')

swagger_view = get_swagger_view(title='API Demo')

urlpatterns = [
    path(r'', include(router_author.urls)),
    path(r'', include(router_book.urls)),

    path(VERSION_API + 'doc', swagger_view),
]
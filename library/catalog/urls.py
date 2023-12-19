from django.urls import path

from . import views
from .views import BookListView, BookSearchView, BookCreateView, AuthorCreateView, AuthorListView, AuthorSearchView

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookSearchView.as_view(), name='book'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorSearchView.as_view(), name='author'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
]


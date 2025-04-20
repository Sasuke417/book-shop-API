from django.urls import path
from the_book_shop_api.inventory import views


urlpatterns = [
    path('genre/', views.GenreList.as_view(), name='genre-list'),
    path('genre/<int:pk>/', views.GenreDetail.as_view(), name='genre-detail'),
    path('authors/', views.AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view(), name='publisher-detail'),
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail')
]
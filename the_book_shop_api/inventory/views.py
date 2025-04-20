
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

from the_book_shop_api.inventory import models, serializers


class PublisherList(ListAPIView):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer


class PublisherDetail(RetrieveAPIView):
    serializer_class = serializers.PublisherSerializer

    def get_queryset(self):
        return models.Publisher.objects.get(pk=self.kwargs['pk'])


class AuthorList(ListAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class AuthorDetail(RetrieveAPIView):
    serializer_class = serializers.AuthorSerializer

    def get_queryset(self):
        return models.Author.objects.get(pk=self.kwargs['pk'])


class GenreList(ListAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class GenreDetail(RetrieveAPIView):
    serializer_class = serializers.GenreSerializer

    def get_queryset(self):
        return models.Genre.objects.filter(id=self.kwargs['pk'])


class BookList(ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()
    
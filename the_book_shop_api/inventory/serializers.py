from rest_framework import serializers
from .models import Book, Author, Publisher, Genre


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        return Book.objects.create(**validated_data)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        return Author.objects.create(**validated_data)


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

    def create(self, validated_data):
        return Publisher.objects.create(**validated_data)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

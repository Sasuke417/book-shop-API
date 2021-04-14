from rest_framework import serializers, validators
from django.contrib.auth.models import User
from .models import Address


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=32,
                                     validators=[validators.UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(validators=[validators.UniqueValidator(queryset=User.objects.all())], required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        return Address.objects.create(**validated_data)

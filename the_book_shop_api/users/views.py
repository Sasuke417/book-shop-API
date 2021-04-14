from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from the_book_shop_api.users.models import Address
from the_book_shop_api.users.serializers import UserSerializer, AddressSerializer


class UserCreate(APIView):
    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressList(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = IsAuthenticated


class AddressDetail(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    permission_classes = IsAuthenticated
    serializer_class = AddressSerializer

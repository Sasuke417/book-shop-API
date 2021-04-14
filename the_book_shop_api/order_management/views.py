from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.response import Response

from the_book_shop_api.order_management import models, serializers


class OrderList(ListCreateAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return models.Order.objects.all()

    def create(self, request, *args, **kwargs):
        if not (request.data.get("url") and len(models.Order.objects.all()) > 1):
            request.data["url"] = request.build_absolute_uri(reverse('order-detail', [1]))
            request.data["user"] = request.user.pk
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'order_id'

    def get_queryset(self):
        return models.Order.objects.get(pk=self.kwargs['order_id'])


class OrderItemList(ListCreateAPIView):
    serializer_class = serializers.OrderItemSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return models.OrderItem.objects.all()

    def create(self, request, *args, **kwargs):
        if not request.data.get("order"):

            request.data["order"] = models.Order.objects.get(pk=1)
        print(models.Order.objects.all())
        print(models.Order.objects.get(pk=1))
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.OrderItemSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return models.OrderItem.objects.get(pk=self.kwargs['item_id'])


class ShipmentList(ListCreateAPIView):
    serializer_class = serializers.ShipmentSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return models.Shipment.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ShipmentDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ShipmentSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return models.Shipment.objects.get(pk=self.kwargs['shipment_id'])

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.response import Response
from django.utils.crypto import get_random_string
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
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return models.OrderItem.objects.filter(
            order__user=self.request.user,
            order__status=models.Order.CART
        )

    def create(self, request, *args, **kwargs):
        # Get or create cart order for the user
        
        order, created = models.Order.objects.get_or_create(
            user=request.user,
            
            defaults={ 'url': "https://www.django-rest-framework.org/"}  
        )
        
        
        item_id = request.data.get('item')
        if not item_id:
            return Response(
                {"detail": "Item ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Check for existing item in cart
            existing_item = models.OrderItem.objects.get(
                order=order,
                item_id=item_id
            )
            existing_item.quantity += 1
            existing_item.save()
            serializer = self.get_serializer(existing_item)
            print("existing")
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except models.OrderItem.DoesNotExist:
            # Create new item in cart
            data = {
                'order': order.pk,
                'item': item_id,
                'quantity': 1
            }
            
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.OrderItemSerializer
    permission_classes = (IsAuthenticated, )

    queryset = models.OrderItem.objects.all()


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
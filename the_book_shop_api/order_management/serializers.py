from rest_framework import serializers
from .models import Order, OrderItem, Shipment
from django.urls import reverse


class OrderItemSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="order.status", read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        return OrderItem.objects.create(**validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return {
            "discount":rep['discount'],
            "order":reverse('orderitem-detail', args={rep['order']}),
            "url":reverse('orderitem-detail', args={rep['order']}),
            "item":reverse('book-detail', args={rep['item']}) ,
            "quantity":rep['quantity'],
            'status':"C"
        }


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
    
    


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'

    def create(self, validated_data):
        return Shipment.objects.create(**validated_data)
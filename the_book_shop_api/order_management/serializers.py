from rest_framework import serializers
from .models import Order, OrderItem, Shipment


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        return OrderItem.objects.create(**validated_data)


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

import factory
from factory import fuzzy
from the_book_shop_api.order_management.models import Order, OrderItem, Shipment
from the_book_shop_api.users.tests.factories import UserFactory, AddressFactory
from the_book_shop_api.inventory.tests.factories import BookFactory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order
    user = factory.SubFactory(UserFactory)
    status = fuzzy.FuzzyChoice([
        Order.CART,
        Order.PROCESSING,
        Order.SHIPPED,
    ])


class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem
    order = factory.SubFactory(OrderFactory)
    item = factory.SubFactory(BookFactory)


class ShipmentFactor(factory.django.DjangoModelFactory):
    class Meta:
        model = Shipment
    user = factory.SubFactory(UserFactory)
    order = factory.SubFactory(OrderFactory)
    address = factory.SubFactory(AddressFactory)

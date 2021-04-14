from test_plus.test import TestCase
from the_book_shop_api.order_management.models import OrderItem, Order, Shipment
from the_book_shop_api.inventory.tests.factories import BookFactory
from the_book_shop_api.order_management.tests.factories import OrderFactory
from the_book_shop_api.users.tests.factories import UserFactory, AddressFactory


class TestModels(TestCase):
    """test to check if all the required fields are declared in each model"""

    def test_create_order(self):
        order = Order.objects.create(user=UserFactory(), status=Order.CART)
        self.assertIsNotNone(order)

    def test_create_orderitem(self):
        order_item = OrderItem.objects.create(order=OrderFactory(), item=BookFactory(), quantity=1,
                                              discount=0.0)
        self.assertIsNotNone(order_item)

    def test_create_shipment(self):
        shipment = Shipment.objects.create(user=UserFactory(), order=OrderFactory(),
                                           address=AddressFactory())
        self.assertIsNotNone(shipment)

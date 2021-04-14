from django.urls import reverse, resolve
from test_plus.test import TestCase


class TestOrderItemURLs(TestCase):
    """Test URL patterns for order_mgmt app."""

    def test_orderitem_list_reverse(self):
        """orderitem-list should reverse to /api/order_mgmt/orderitem/."""
        self.assertEqual(reverse('orderitem-list'), '/api/order_mgmt/orderitem/')

    def test_orderitem_list_resolve(self):
        """/api/order_mgmt/orderitem/ should resolve to orderitem-list."""
        self.assertEqual(resolve('/api/order_mgmt/orderitem/').view_name, 'orderitem-list')

    def test_orderitem_detail_reverse(self):
        """orderitem-detail should reverse to /api/order_mgmt/orderitem/1/."""
        self.assertEqual(reverse('orderitem-detail', args={1}), '/api/order_mgmt/orderitem/1/')

    def test_orderitem_detail_resolve(self):
        """/api/order_mgmt/orderitem/1/ should resolve to orderitem-detail."""
        self.assertEqual(resolve('/api/order_mgmt/orderitem/1/').view_name, 'orderitem-detail')


class TestOrderURLs(TestCase):
    """Test URL patterns for order_mgmt app."""

    def test_order_list_reverse(self):
        """order-list should reverse to /api/order_mgmt/order/."""
        self.assertEqual(reverse('order-list'), '/api/order_mgmt/order/')

    def test_order_list_resolve(self):
        """/api/order_mgmt/order/ should resolve to order-list."""
        self.assertEqual(resolve('/api/order_mgmt/order/').view_name, 'order-list')

    def test_order_detail_reverse(self):
        """order-detail should reverse to /api/order_mgmt/order/1/."""
        self.assertEqual(reverse('order-detail', args={1}), '/api/order_mgmt/order/1/')

    def test_order_detail_resolve(self):
        """/api/order_mgmt/order/1/ should resolve to order-detail."""
        self.assertEqual(resolve('/api/order_mgmt/order/1/').view_name, 'order-detail')


class TestShipmentURLs(TestCase):
    """Test URL patterns for shipment_mgmt app."""

    def test_shipment_list_reverse(self):
        """shipment-list should reverse to /api/order_mgmt/shipment/."""
        self.assertEqual(reverse('shipment-list'), '/api/order_mgmt/shipment/')

    def test_shipment_list_resolve(self):
        """/api/order_mgmt/shipment/ should resolve to shipment-list."""
        self.assertEqual(resolve('/api/order_mgmt/shipment/').view_name, 'shipment-list')

    def test_shipment_detail_reverse(self):
        """shipment-detail should reverse to /api/order_mgmt/shipment/1/."""
        self.assertEqual(reverse('shipment-detail', args={1}), '/api/order_mgmt/shipment/1/')

    def test_order_detail_resolve(self):
        """/api/order_mgmt/shipment/1/ should resolve to shipment-detail."""
        self.assertEqual(resolve('/api/order_mgmt/shipment/1/').view_name, 'shipment-detail')

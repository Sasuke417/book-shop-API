from django.urls import reverse, resolve

from test_plus.test import TestCase


class TestUserURLs(TestCase):
    """Test URL patterns for users"""

    def test_user_create_reverse(self):
        """user-create should reverse to /api/users/signup/."""
        self.assertEqual(reverse('user-create'), '/api/users/signup/')

    def test_user_create_resolve(self):
        """/api/users/signup/ should resolve to user-create."""
        self.assertEqual(resolve('/api/users/signup/').view_name, 'user-create')

    def test_user_signin_reverse(self):
        """account_login should reverse to /api/users/signin/."""
        self.assertEqual(reverse('account_login'), '/api/users/signin/')

    def test_user_signin_resolve(self):
        """/api/users/signin/ should resolve to account_login."""
        self.assertEqual(resolve('/api/users/signin/').view_name, 'account_login')


class TestAddressURLs(TestCase):
    """Test URL patterns for address"""

    def test_address_list_reverse(self):
        """address-list should reverse to /api/users/address/."""
        self.assertEqual(reverse('address-list'), '/api/users/address/')

    def test_address_list_resolve(self):
        """/api/users/address/ should resolve to address-list."""
        self.assertEqual(resolve('/api/users/address/').view_name, 'address-list')

    def test_address_detail_reverse(self):
        """address-detail should reverse to /api/users/address/1/."""
        self.assertEqual(reverse('address-detail', args={1}), '/api/users/address/1/')

    def test_order_detail_resolve(self):
        """/api/users/address/1/ should resolve to address-detail."""
        self.assertEqual(resolve('/api/users/address/1/').view_name, 'address-detail')

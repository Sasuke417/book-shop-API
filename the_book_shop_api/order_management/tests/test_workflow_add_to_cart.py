from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from the_book_shop_api.order_management.models import Order
from the_book_shop_api.inventory.tests.factories import BookFactory


class CartWorkflow(APITestCase):
    def setUp(self):
        data = {
                    'username': 'testuser',
                    'email': 'test@tcs.com',
                    'password': 'tata1234'
                }

        response = self.client.post(reverse('user-create'), data, format='json')
        self.header = {
            'HTTP_AUTHORIZATION': 'Token {}'.format(response.data['token'])
            }
        self.add_to_cart_url = reverse('orderitem-list')

    def test_add_item_auth(self):
        response = self.client.get(self.add_to_cart_url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.post(self.add_to_cart_url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_add_book_to_cart(self):
        item = BookFactory()
        response = self.client.post(self.add_to_cart_url,
                                    {'item': item.pk},
                                    **self.header, format='json')
        data = response.data
        self.assertIsNotNone(data)
        # check default value
        self.assertEquals(data.get('quantity'), 1)
        # hyperlinked order
        order_url = data.get('order')
        response = self.client.get(order_url, **self.header)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        order_status = response.data.get('status')
        self.assertEquals(order_status, Order.CART)
        # hyperlinked item
        item_url = data.get('item')
        response = self.client.get(item_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('title'), item.title)

    def test_add_second_book_to_cart(self):
        item = BookFactory()
        # add 1st item
        response = self.client.post(self.add_to_cart_url,
                                    {'item': item.pk},
                                    **self.header, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        # get the order url
        order_url = response.data.get('order')
        # add 2nd item
        response = self.client.post(self.add_to_cart_url,
                                    {'item': BookFactory().pk},
                                    **self.header, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        # items should add to same order
        self.assertEquals(order_url, response.data.get('order'))

    def test_add_same_second_book_to_cart(self):
        item = BookFactory()
        # add 1st item
        response = self.client.post(self.add_to_cart_url,
                                    {'item': item.pk},
                                    **self.header, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        # add 2nd item
        response = self.client.post(self.add_to_cart_url,
                                    {'item': item.pk},
                                    **self.header, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        # items should add to same item
        self.assertEquals(response.data.get('quantity'), 2)

    def test_remove_item(self):
        # add 1st item
        response = self.client.post(self.add_to_cart_url,
                                    {'item': BookFactory().pk},
                                    **self.header, format='json')
        # add 2nd item
        response = self.client.post(self.add_to_cart_url,
                                    {'item': BookFactory().pk},
                                    **self.header, format='json')
        item_url = response.data.get('url')
        response = self.client.get(self.add_to_cart_url,
                                   **self.header, format='json')
        # let see if two items are in cart
        self.assertEquals(len(response.data), 2)
        # now deleting one
        response = self.client.delete(item_url, **self.header)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(self.add_to_cart_url,
                                   **self.header, format='json')
        # let see if two items are in cart
        self.assertEquals(len(response.data), 1)


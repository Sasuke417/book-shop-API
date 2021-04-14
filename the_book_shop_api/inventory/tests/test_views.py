from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestGenre(APITestCase):
    fixtures = ['seed_data.json']

    def test_list(self):
        url = reverse('genre-list')
        response = self.client.get(url)
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 2)

    def test_detail(self):
        url = reverse('genre-detail', args=[1])
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('tag'), 'fiction')
        self.assertIsNotNone(response.data.get('description'))


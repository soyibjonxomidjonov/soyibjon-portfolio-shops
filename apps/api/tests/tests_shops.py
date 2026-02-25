from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from apps.shops_app.models import Shop
from django.utils.text import slugify


User = get_user_model()

class ShopsTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass', is_staff=True)
        self.user2 = User.objects.create_user(username='testuser2', password='testpass2', is_staff=True)

        self.client.force_authenticate(user=self.user)
        # self.client.force_authenticate(user=self.user2)

        self.shop1 = Shop.objects.create(owner=self.user, name="Anvar Electronics")
        self.shop2 = Shop.objects.create(owner=self.user, name="Anvar Food")
        self.shop3 = Shop.objects.create(owner=self.user, name="Anvar Books")

        self.shop4 = Shop.objects.create(owner=self.user2, name="Gilos Do'koni")


    def test_shops_list(self):
        url = reverse('shops-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)
        self.assertEqual(response.data['results'][0]['name'], "Anvar Electronics")
        self.assertIn('anvar', response.data['results'][0]['slug'])



    def test_shops_detail(self):
        url = reverse('shops-detail', args=[self.shop2.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Anvar Food")



    def test_shops_update(self):
        url = reverse('shops-detail', args=[self.shop2.pk])
        data = {'name': 'Test shops Updated'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test shops Updated')




    def test_shops_create(self):
        url = reverse('shops-list')
        data = {'name': "Test shop"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_shops_delete(self):
        url = reverse('shops-detail', args=[self.shop3.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)











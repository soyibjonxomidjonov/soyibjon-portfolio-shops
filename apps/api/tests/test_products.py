from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from apps.shops_app.models import Product, Shop
from django.utils.text import slugify


User = get_user_model()

class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user2 = User.objects.create_user(username='testuser2', password='testpass2')

        self.client.force_authenticate(user=self.user)


        self.shop = Shop.objects.create(name='Test Shop', description='test-description', address='test-adres', owner=self.user)
        self.shop2 = Shop.objects.create(name='Test Shop2', description='test-description2', address='test-adres2', owner=self.user2)

        self.product1 = Product.objects.create(
            shop=self.shop,
            name="Olma",
            description="Qizil olma",
            price=12000,
            stock=100,
            unity='kg'
        )

        self.product2 = Product.objects.create(
            shop=self.shop,
            name="Non",
            price=3000,
            stock=50
        )

        self.product3 = Product.objects.create(
            shop=self.shop,
            name="Sut",
            description="1 litrlik qadoqda",
            price=9000,
            stock=20,
            unity='litr'
        )

    def test_products_list(self):
        url = reverse('products-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)
        self.assertEqual(response.data['results'][0]['name'], "Sut")
        self.assertEqual(response.data['results'][0]['price'], 9000)

    def test_products_detail(self):
        url = reverse('products-detail', args=[self.product2.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Non")

    def test_products_update(self):
        url = reverse('products-detail', args=[self.product2.pk])
        data = {'shop':self.shop.id,
            'name':"Ananas",
            'price':20000,
            'unity':'dona'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Ananas')
        self.assertEqual(response.data['unity'], 'dona')
        self.assertEqual(response.data['price'], 20000)


    def test_products_update_bad_request(self):
        url = reverse('products-detail', args=[self.product2.pk])
        data = {'shop':self.shop2.id,
            'name':"Ananas",
            'price':20000,
            'unity':'dona'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_products_create(self):
        url = reverse('products-list')
        data = {'shop':self.shop.id,
            'name':"Uzum",
            'description':"Suvli yangi uzum",
            'price':70000,
            'stock':50,
            'unity':'kg'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_products_delete(self):
        url = reverse('products-detail', args=[self.product3.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_products_search(self):
        url = reverse('products-list') + '?search=Non'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Non')

    def test_products_update_bad_price(self):
        url = reverse('products-detail', args=[self.product2.pk])
        data = {'shop':self.shop.id,
            'name':"Ananas",
            'price':-20000,
            'unity':'dona'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

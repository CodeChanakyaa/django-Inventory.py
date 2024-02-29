from django.test import TestCase
import json


class AppTest(TestCase):
    def test_1_inventory_get_success(self):
        res = self.client.get('/inventory/items/')
        print(res.json())
        assert b'[]' in res.content
        assert 200 == res.status_code

    def test_2_inventory_post_success(self):
        data={'name': 'shirt', 'category': 'top wear', 'price': 500, 'discount': 50, 'quantity': 10, 'barcode': 12345678}
        res = self.client.post('/inventory/items/', data=json.dumps(data), content_type='application/json')
        print(res.json())
        assert 'shirt' == res.json()['name']
        assert 201 == res.status_code

    def test_3_inventory_delete_success(self):
        res = self.client.post('/inventory/items/', data={'name': 'shirt', 'category': 'top wear', 'price': 500, 'discount': 50, 'quantity': 10, 'barcode': 12345678})
        res = self.client.delete('/inventory/items/1/')
        assert 204 == res.status_code

    def test_4_inventory_post_error(self):
        res = self.client.post('/inventory/items/', data={'name': 'shirt', 'category': 'top wear', 'price': 500, 'discount': 50, 'quantity': 10, 'barcode': 12345678})
        res = self.client.post('/inventory/items/', data={'name': 't-shirt', 'category': 'top wear', 'price': 500, 'discount': 50, 'quantity': 10, 'barcode': 12345678})
        print(res.json())
        assert b'"inventory item with this barcode already exists.' in res.content
        assert 400 == res.status_code

    def test_5_inventory_get_sort_success(self):
        res = self.client.post('/inventory/items/', data={'name': 'shirt', 'category': 'top wear', 'price': 700, 'discount': 50, 'quantity': 10, 'barcode': 12345678})
        res = self.client.post('/inventory/items/', data={'name': 't-shirt', 'category': 'top wear', 'price': 1300, 'discount': 50, 'quantity': 10, 'barcode': 12345764})
        reponse = self.client.get('/items/sort/')
        print(reponse.json())
        assert 1300 == reponse.json()[0]['price']
        assert 700 == reponse.json()[1]['price']
        assert 200 == reponse.status_code

    def test_6_inventory_get_query_category_success(self):
        res = self.client.post('/inventory/items/', data={'name': 'shirt', 'category': 'top wear', 'price': 500, 'discount': 50, 'quantity': 10, 'barcode': 12345678})
        res = self.client.post('/inventory/items/', data={'name': 't-shirt', 'category': 'top wear', 'price': 700, 'discount': 50, 'quantity': 10, 'barcode': 123456789})
        res = self.client.post('/inventory/items/', data={'name': 'shorts', 'category': 'bottom wear', 'price': 1300, 'discount': 50, 'quantity': 10, 'barcode': 125678678})
        response = self.client.get('/items/query/top%20wear/')
        print(response.json())

        assert 'shirt' in response.json()[0]['name']
        assert 't-shirt' in response.json()[1]['name']
        assert 200 == response.status_code
        assert len(response.json()) == 2

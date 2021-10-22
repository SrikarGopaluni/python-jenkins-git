from unittest import TestCase
from mypage2 import app
import json


class ProductTest(TestCase):
    def test_welcome(self):
        with app.test_client() as c:
            resp = c.get("/api/products")
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), [{"productId": 1, "productName": "Iphone", "price": 135000, "rating": 4.8}, {"productId": 2, "productName": "Oneplus", "price": 150000, "rating": 4.5}, {"productId": 3, "productName": "Samsung", "price": 70000, "rating": 4}, {"productId": 4, "productName": "MI", "price": 50000, "rating": 4.2}, {"productId": "5", "productName": "Dell", "price": "200000", "rating": "4.8"}])

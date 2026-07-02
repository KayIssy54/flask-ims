import unittest
import json
from app import app


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_get_inventory(self):
        response = self.client.get("/inventory")
        self.assertEqual(response.status_code, 200)

    def test_post_inventory(self):
        response = self.client.post(
            "/inventory",
            json={
                "name": "Test Product",
                "barcode": "123456789",
                "price": 100,
                "stock": 20
            }
        )

        self.assertEqual(response.status_code, 201)

    def test_patch_inventory(self):
        response = self.client.patch(
            "/inventory/1",
            json={
                "price": 250
            }
        )

        self.assertIn(response.status_code, [200, 404])

    def test_delete_inventory(self):
        response = self.client.delete("/inventory/1")

        self.assertIn(response.status_code, [200, 404])


if __name__ == "__main__":
    unittest.main() 
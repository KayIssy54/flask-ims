import unittest
from unittest.mock import patch
from services import fetch_product_from_api


class ServiceTestCase(unittest.TestCase):

    @patch("services.requests.get")
    def test_fetch_product(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "status": 1,
            "product": {
                "product_name": "Milk",
                "brands": "Brookside",
                "ingredients_text": "Milk",
                "quantity": "500ml",
                "categories": "Dairy"
            }
        }

        product = fetch_product_from_api("12345")

        self.assertEqual(product["product_name"], "Milk")
        self.assertEqual(product["brands"], "Brookside")


if __name__ == "__main__":
    unittest.main()
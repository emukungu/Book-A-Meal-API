import unittest 
from app import app, views, models
import json


class Orders(unittest.TestCase):
    def setUp(self):
        self.test = app.test_client()

    def test_empty_order(self):
        result = self.test.post(
            "/api/v1/orders", 
            data = json.dumps({"order": ""}), 
            content_type = "application/json"
        )
        self.assertEqual(result.status_code, 400)

    def test_get_empty_order(self):
        result = self.test.get("/api/v1/orders")
        #print(result.data)
        self.assertEqual(result.status_code, 404) 

    def test_correct_order(self):
        result = self.test.post(
            "/api/v1/orders", 
            data = json.dumps({"order": "['beef', 'goat']"}), 
            content_type = "application/json"
        )   
        self.assertEqual(result.status_code, 200)

    def test_get_order(self):
        result = self.test.get("/api/v1/orders")
        self.assertEqual(result.status_code, 200)

    def test_empty_order_update(self):
        result = self.test.put(
            "/api/v1/orders/orderid", 
            data = json.dumps({"orders": ""}), 
            content_type = "application/json"
        )
        self.assertEqual(result.status_code,400)

    def test_correct_order_update(self):
        result = self.test.put(
            "/api/v1/orders/orderid", 
            data = json.dumps({"orders": "['beef']"}), 
            content_type = "application/json"
        )
        self.assertEqual(result.status_code,200)

if __name__ == "__main__":
    unittest.main()

    
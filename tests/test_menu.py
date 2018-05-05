import unittest 
from app import app, views, models
import json


class Menu(unittest.TestCase):
    def setUp(self):
        self.test = app.test_client()

    def test_empty_menu(self):
        result = self.test.post(
            "/api/v1/menu", 
            data = json.dumps({"menu_title":"", "menu_items":[]}), 
            content_type = "application/json"
        )
        self.assertEqual(result.status_code, 400)

    def test_get_empty_menu(self):
        result = self.test.get("/api/v1/menu")
        self.assertEqual(result.status_code, 204) 

    def test_set_the_menu(self):
        result = self.test.post(
            "/api/v1/menu", 
            data = json.dumps({"menu_title":"Italian", "menu_items":["beef", "goat", "chicken"]}), 
            content_type = "application/json"
        )
        print(result.data)   
        self.assertEqual(result.status_code, 200)

    def test_get_menu(self):
        result = self.test.get("/api/v1/menu")
        print(result.data)
        self.assertEqual(result.status_code, 200)

if __name__ == "__main__":
    unittest.main()


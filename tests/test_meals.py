import unittest 
from app import app, views, models
import json


class Meals(unittest.TestCase):
    def setUp(self):
        self.test = app.test_client()

    def test_add_empty_meal(self):
        result = self.test.post(
            "/api/v1/meals", 
            data = json.dumps({"meal_name":"", "price":""}), 
            content_type = "application/json"
        )
        self.assertEqual(result.status_code, 400)

    def test_add_right_meal(self):
        result = self.test.post(
            "/api/v1/meals", 
            data = json.dumps({"meal_name":"rice", "price":"2000"}), 
            content_type = "application/json"
        )
        self.assertEqual(result.status_code, 200)

    def test_get_available_meals(self):
        result = self.test.get("/api/v1/meals")
        print(result.data)
        self.assertEqual(result.status_code, 200)

    def test_empty_update_meal(self):
        result = self.test.put(
            "/api/v1/meals/1", 
            data = json.dumps({"price":""}), 
            content_type = "application/json"
        )
        print(result.data)
        self.assertEqual(result.status_code,400)

    def test_correct_update_meal(self):
        result = self.test.put(
            "/api/v1/meals/1", 
            data = json.dumps({"price":"4000"}), 
            content_type = "application/json"
        )
        print(result.data)
        self.assertEqual(result.status_code,200)
    
    #def test_empty_delete_meal(self):
    #    result = self.test.delete(
     #       "/api/v1/meals/<int:meal_id>", 
      #      data = json.dumps({"meal_name":""}), 
       #     content_type = "application/json"
        #)
        #self.assertEqual(result.status_code,400)

    def test_correct_delete_meal(self):
        result = self.test.delete(
            "/api/v1/meals/1"
        )
        print(result.data)
        self.assertEqual(result.status_code,200)


if __name__ == "__main__":
    unittest.main()
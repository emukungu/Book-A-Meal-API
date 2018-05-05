import unittest 
from app import app
from app import views, models
import json



class User(unittest.TestCase):
    def setUp(self):
        self.test = app.test_client()

           
    def test_signup_empty_fields(self):
       
        res = self.test.post(
            "/api/v1/auth/signup", 
            data = json.dumps({'firstName': "", 'password':"", 'lastName':''}), 
            content_type = 'application/json'
        )
        self.assertEqual(res.status_code, 400)

    def test_signup_filled_fields(self):
        result = self.test.post(
            "/api/v1/auth/signup", 
            data = json.dumps({"user_id":1,"firstName": "Esther", "password": "mukungu", "lastName":"Namusisi", "username":"essy"}), 
            content_type ='application/json'
        )
        print(result.data)
        self.assertEqual(result.status_code, 201)

    def test_login_empty_users(self): 
        result = self.test.post(
            "/api/v1/auth/login", 
            data = json.dumps({'username':'', 'password':''}),
             content_type = 'application/json'
        )
        self.assertEqual(result.status_code, 401)
    
    def test_login_correct(self):        
        result = self.test.post(
            "/api/v1/auth/login",
             data = json.dumps({"username":"enmukungu", "password":"muk"}), 
             content_type = 'application/json'
        )
        self.assertEqual(result.status_code, 200)

if __name__ == "__main__":
    unittest.main()
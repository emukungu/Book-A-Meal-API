from flask import Flask

app = Flask(__name__)

# This will hold all users created on signup
user_list = []
meal_list =[]
menu_list = []
orders_list = []

from .views import auth, meals, menu, orders
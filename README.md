[![Coverage Status](https://coveralls.io/repos/github/emukungu/Book-A-Meal-API/badge.svg?branch=dev)](https://coveralls.io/github/emukungu/Book-A-Meal-API?branch=dev) [![Build Status](https://travis-ci.org/emukungu/Book-A-Meal-API.svg?branch=dev)](https://travis-ci.org/emukungu/Book-A-Meal-API)


# Book-A-Meal-API
About

Book-A-Meal is an application that allows customers to make food orders and helps the food vendor know what the customer wants

Purpose

The API is to provide a standard API interface to manage booking a meal from any catering service by any user.

Features

With this API;

You are able to create accounts for both the user and caterer

The user is able to view and make his order

The caterer is able to add meals, set the menu, receive users' orders 
 
Prerequisites for the development of this API are:

Flask - a python framework

Requirements

Python 3 and above

Tests

For Agile development, we run tests and to run the API tests, go to command line and run the commands below

    $ cd tests/
    $ pytest

Running the application

To run the appilacation on Windows

Clone the git repository at https://github.com/emukungu/Book-A-Meal-API/tree/dev to your local machine

On the terminal type the following commands:

$ cd Book-A-Meal-API

$ pip install virtualenv

$ activate

$ pip install -r requirements.txt

$ python run.py



API endpoints created

| API endpoints | Description|
|------|--------|
|POST /auth/signup| Register a user|
|POST /auth/login| Login user|
|GET /meals| Get all meal options|
|POST /meals| Add a meal|
|PUT /meals/<mealid>| Update the information of a meal option|
|DELETE /meals/<mealid>| Remove a meal option|
|GET /menu| Get menu for the day|
|POST /menu| Setup menu for the day|
|GET /orders| Get all orders|
|POST /orders| Select a meal option from the menu|
|PUT /orders/orderid| Modify an order|






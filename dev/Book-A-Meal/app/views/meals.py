from flask import jsonify, request, json
from app import app, meal_list
from app.models import models
from app.models.models import Meals

@app.route("/api/v1/meals", methods = ['POST'])
def add_meal():
    response = {
        'message': ''
    }
    if request.method == 'POST':
        
        data = request.json
        meal_name = data["meal_name"]
        price = data["price"]


        if (meal_name == "" and price == "") or (meal_name == None and price == None):
            response = {
                'message': 'Meal details are empty'
            }
            print(meal_name)
            print(price)
            return jsonify(response),400
        else: 
            meals = Meals(meal_name = meal_name, price = price)
            meal_list.append(meals)
            response['message'] = 'Meal added'

            return jsonify(response),200


@app.route("/api/v1/meals", methods = ['GET'])
def get_meal():
    response = {
        'message': ''
    }
    get_all_meals = []
    if request.method == 'GET':        
        if len(meal_list) >0:
            for meal in meal_list:
                get_all_meals.append({
                    "name": meal._meal_name,
                    "price": meal._price
                    })
            response['all meals'] = get_all_meals
            return jsonify(response),200
        else:
            print(meal_list)
            response['message'] = "No meals available"
            return jsonify(response),404

@app.route("/api/v1/meals/mealid", methods=['PUT'])
def put_meal():
    response = {
        "status" : "fail",
        "message" : "No changes done"
    }
    if request.method == 'PUT': #update already existing meal
        
        data = request.json
        meal_name = data.get('meal_name')
        price = data.get("price")
        if price == "" or price == None:
            response['message'] = "Invalid update"

            return jsonify(response),400

        else:
                      
            for meal in meal_list:
                if meal._meal_name == meal_name:
                    meal._price = price

                    print(meal._meal_name)
                    print(meal._price)
            response['message'] = 'Meal has been updated'
            return jsonify(response), 200

@app.route("/api/v1/meals/mealid", methods=['DELETE'])
def delete_meal():
    response = {
        "message" : ""
    }
             
    data = request.json
    meal_name = data.get('meal_name')
    if meal_name == "" or meal_name == None:
        response['message'] = "Invalid delete"

        return jsonify(response),400

    else:            
        for meal in meal_list:
            if meal._meal_name == meal_name:
                meal._price = ""
                meal._meal_name = ""

                print(meal._meal_name)
                print(meal._price)
        response['message'] = 'Meal has been deleted'
        return jsonify(response), 200
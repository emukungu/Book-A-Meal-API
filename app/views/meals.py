from flask import jsonify, request, json
from app import app
from app import meal_list
from app.models import models
#from app.views.auth import logged
from app.models.models import Meals

@app.route("/api/v1/meals", methods = ['POST'])
#@logged
def add_meal():
    response = {
        'message': ''
    }
    if request.method == 'POST':
        
        data = request.json
        meal_name = data["meal_name"]
        price = data["price"]      

        if meal_name == "" and price == "":
            response = {
                'message': 'Meal details are empty'
            }
            return jsonify(response),400
        else:
            meals = Meals(meal_name= meal_name, price = price)
            meal_list.append(meals)
            for meal in meal_list:
                meal._meal_id += 1
            response['message'] = 'Meal added'

            return jsonify(response),200


@app.route("/api/v1/meals", methods = ['GET'])
def get_meal():
    response = {
        'message': ''
    }        
    if request.method == 'GET':
        get_all_meals = []        
        if len(meal_list) >0:
            for meal in meal_list:
                get_all_meals.append({
                    "name": meal._meal_name,
                    "price": meal._price,
                    "meal_id": meal._meal_id
                    })
            response['all meals'] = get_all_meals
            return jsonify(response), 200
        else:
            print(meal_list)
            response['message'] = "No meals available"
            return jsonify(response),204

@app.route("/api/v1/meals/<int:meal_id>", methods=['PUT'])
def put_meal(meal_id):
    response = {
        "status" : "fail",
        "message" : "No changes done"
    }
    if request.method == 'PUT': #update already existing meal
        
        data = request.json
        #meal_name = data.get('meal_name')
        price = data.get("price")
        #meal_id = data.get("meal_id")
        if price == "" or price == None:
            response['message'] = "Invalid update"

            return jsonify(response),400

        else:      
            for meal in meal_list:                
                if meal_id == meal._meal_id:
                    meal._price = price
                    response['message'] = 'Meal has been updated'
            return jsonify(response), 200

@app.route("/api/v1/meals/<int:meal_id>", methods=['DELETE'])
def delete_meal(meal_id):
    response = {
        "message" : ""
    }
    if request.method == 'DELETE':
                
        for meal in meal_list:
            if meal._meal_id == meal_id:
                meal._price = None
                meal._meal_name = None
                meal._meal_id = 0
        response['message'] = 'Meal has been deleted'
        return jsonify(response), 200
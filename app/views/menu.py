from flask import jsonify, request, json
from app import app, menu_list, meal_list
from app.models import models
from app.models.models import Menu

@app.route("/api/v1/menu", methods =['POST'])
def setup_menu():
    response = {
        "message": ""
    }
    if request.method == 'POST':
        
        data = request.json
        menu_title = data["menu_title"]
        menu_items = data["menu_items"]
        if menu_title == "":
            response['message'] = "No menu has been set"

            return jsonify(response),400

        else:
            menu = Menu(menu_title = menu_title)
            for item in menu_items:
                for meal in meal_list:
                    if item == meal._meal_name:
                        menu._menu_items.append({
                            "meal name": item,
                            "price": meal._price
                        })
                        menu_list.append(menu)
                        response["message"] = "Menu successfully set."
            return jsonify(response), 200
                    

@app.route("/api/v1/menu", methods = ['GET'])
def get_menu():
    response = {
            "message":""
    }
    if len(menu_list) > 0:
        menus = []
        for item in menu_list:
            print(item.menu())
            menus.append(item.menu())
        
        #response["menu"] : menus
        return jsonify(menus), 200
    else:
        
        response['message'] = "No menu available"
        return jsonify(response), 404

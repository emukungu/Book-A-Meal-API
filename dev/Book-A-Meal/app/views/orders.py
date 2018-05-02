from flask import jsonify, request, json
from app import app, orders_list, meal_list
from app.models import models
from app.models.models import Orders

@app.route("/api/v1/orders", methods = ["POST"])
def orders():
    response = {
        "message": ""
    }
    data = request.json
    order = data["order"]
    
    if order == "" or order == None:
        response['message'] = "No orders"

        return jsonify(response),400

    else:
        orders = Orders(items = order)
        for item in order:
            for meal in meal_list:
                if item == meal._meal_name:
                    orders._total += meal._price
        orders_list.append(orders)
        response["message"] : "Orders successfully set."
        return jsonify(response), 200

@app.route("/api/v1/orders", methods = ['GET'])
def get_orders():
    response = {
        'message': ''
    }
    get_orders = []
    if request.method == 'GET':        
        if len(orders_list) >0:
            for order in orders_list:
                get_orders.append({
                    "items" : order._items,
                    "total price" : order._total
                })
            response['message'] = get_orders
            return jsonify(response),200
        else:
            
            response['message'] = "No orders made"
            return jsonify(response),404

@app.route("/api/v1/orders/orderid", methods=['PUT'])
def modify_order():
    response = {
        "status" : "fail",
        "message" : "No changes done"
    }
    data = request.json
    orders = data.get('orders')
    if orders == "" or orders == None:
        response['message'] = "Invalid update"

        return jsonify(response), 400

    else:
        orders_list.append(Orders(items=orders))
        for item in orders:
            for meal in meal_list:
                for menu_order in orders_list:
                    if meal._meal_name == item:
                        menu_order._total += meal._price

        response['message'] = 'Order has been updated'
        return jsonify(response), 200

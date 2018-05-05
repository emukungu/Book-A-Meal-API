from flask import jsonify, request, json
from app import app
from app import orders_list, meal_list
from app.models import models
from app.models.models import Orders

@app.route("/api/v1/orders", methods = ["POST"])
def orders():
    response = {
        "message": ""
    }
    if request.method == 'POST':
        data = request.json
        order = data["order"]
    
        if order == []:
            response['message'] = "Enter your orders"

            return jsonify(response),400

        else:
            orders = Orders(items = order)
            for item in order:
                for meal in meal_list:
                    if item == meal._meal_name:
                        orders._total += float(meal._price)
                        orders_list.append(orders)
                        response["message"] = "Orders successfully set."
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
            response['status'] = "successful"
            return jsonify(response), 404

@app.route("/api/v1/orders/<int:order_id>", methods=['PUT'])
def modify_order(order_id):
    response = {
        "status" : "fail",
        "message" : "No changes done"
    }
    update_order = []
    for meal in meal_list:
        for order in orders_list:
            if meal._meal_id == order_id:
                    order._total += float(meal._price)
                    update_order.append(meal._meal_name)
    orders_list.append(Orders(items= update_order))

    response['message'] = 'Order has been updated'
    response['status'] = "successful"
    return jsonify(response), 200

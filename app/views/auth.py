from flask import jsonify, request, json
#from flask_jwt import JWT, jwt_required
from app import app, user_list
from app.models import models
from app.models.models import User


@app.route("/api/v1/auth/signup", methods=['POST'])
def signup():
    response = {
        'message':''
    }
    if request. method == 'POST':
        data = request.json
    
        firstName = data['firstName'] 
        lastName = data['lastName']
        password = data['password']
        user_id = data['user_id']
        username = data['username']
    
        if firstName == '' or lastName == '' or password == '' or username == '' or user_id == '' :
            response = {
                'message': 'Empty'
            }
            return jsonify(response),400
        else:
            user = User(user_id = user_id, firstName=firstName, lastName=lastName, password=password, username = username)
            user_list.append(user)
            response['message'] = 'User created'

            return jsonify(response),201
   
            
@app.route("/api/v1/auth/login", methods = ['POST'])
def login():
    response = {
        'message':''
    }
    data = request.json
    username = data['username']
    password = data['password']

    if username == '' and password == '':
        response = {
            'message': 'Empty'
        }
        return jsonify(response),401
    else:
        #response['message'] = 'User logged in'

        return jsonify(response),200

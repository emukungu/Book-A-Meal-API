from flask import jsonify, request, json
from app import app, user_list
from app.models import models
from app.models.models import User, User_logged_in
#from models import User, User_logged_in


@app.route("/api/v1/auth/signup", methods=['POST'])
def signup():
    response = {
        'message':''
    }
    data = request.json
    
    firstName = data['firstName'] 
    lastName = data['lastName']
    password = data['password']
    
    if firstName == '' and lastName == '' and password == '':
        response = {
            'message': 'Empty'
        }
        return jsonify(response),400
    else:
        user = User(firstName=firstName, lastName=lastName, password=password)
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

    if username == '' and password == '' or username == None and password == None:
        response = {
            'message': 'Empty'
        }
        return jsonify(response),401
    else:
        user = User_logged_in(username=username, password=password)
        user_list.append(user)
        response['message'] = 'User logged in'

        return jsonify(response),200

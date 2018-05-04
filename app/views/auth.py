from flask import jsonify, request, json
#from flask_jwt import jwt
#import datetime
from functools import wraps
from app import app, user_list
from app.models import models
from app.models.models import User, User_logged_in

#from models import User, User_logged_in

#secret key
app.config['SECRET_KEY'] = 'secretkey'
#creating a decorator function for the view function(func)
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        #get token using querry string
        token = request.args.get('token')
        
        if not token:
            return jsonify({"message":"Token is missing"}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({"message": "Tokken is Invalid"}), 401

        return func(*args, **kwargs) #view function

    return with_logging        


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

    if username == '' and password == '':
        response = {
            'message': 'Empty'
        }
        return jsonify(response),401
    else:
        auth = request.authorization
        if auth and auth.username == "username" and auth.password == "password": #verify authentication
            token = jwt.encode({"user": auth.username, "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=15)},
            app.config('SECRET_KEY')
            )#actual user who logged in; payload info; use default encoding algorithm
            response['token'] = token.decode('UTF-8')
            user = User_logged_in(username=username, password=password)
            user_list.append(user)
            response['message'] = 'User logged in'

        return jsonify(response),200

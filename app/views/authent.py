from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
#from werkzeug.security import safe_str_cmp
from app import app, user_list

app.config['SECRET_KEY'] = 'bootcamp'
app.config['JWT_AUTH_URL_RULE'] = '/api/v1/auth/login'
jwt = JWT(app, logged, identity)

def logged(username, password):
    for user in user_list:
        if user.username == username and user.password == password:
            return user

def identity(payload): #identifying user
    user_id = payload['identity']
    for user in user_list:
        if user._id == user_id:
            return user


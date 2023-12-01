
from flask import request
from models.user_model import register_user, login_user, check_user_exists
from config import db_config
from services.jwt_handler import signJWT


def register():    
    """
    Register user
    """
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not all([username, email, password]):
        return {"error": "Missing data"}, 400

    if check_user_exists(db_config, username):
        return {"error": "User already exists"}, 400
    
    register_user(db_config, username, email, password)
    return {"message": "User registered successfully"}, 201

def login():
    """
    Login user
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not all([username, password]):
        return {"error": "Missing data"}, 400

    user = login_user(db_config, username, password)
    if user:
        user_id = user['user_id']
        token = signJWT(user_id,username, password)
        return token, 200
    else:
        return {"error": "Invalid username or password"}, 401

    

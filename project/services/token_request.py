from flask import request
from functools import wraps 
from .jwt_handler import decodeJWT
from models.user_model import get_all_users
from config import db_config
def token_required(f):
    """
    Token required decorator to check if token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        all_users = get_all_users(db_config)

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
            decodedtoken = decodeJWT(token)
        
        if not token:
            return {'message': 'Token is missing'}, 401
        
        if  decodedtoken == {}:
            return {'message' : 'Your token is wrong!!!'}, 401
        for item in all_users:
            if decodedtoken['username'] == item['username'] or decodedtoken['password'] == item['password']:
                return f(*args, **kwargs)
        return {'message' : 'Your token is wrong!!!'}, 401
        
    return decorated
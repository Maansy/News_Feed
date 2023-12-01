import jwt
from dotenv import load_dotenv
import os

load_dotenv()


JWT_SECRET = os.getenv('JWT_SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')

def token_response(token:str):
    """
    Generates the Token Response
    """
    return{
        'access token' : token
    }

def signJWT(user_id:int,username:str,password:str):
    """
    Generates the JWT Token
    :param username: username
    :param password: password
    """
    payload = {
        'user_id':user_id,
        'username':username,
        'password':password
        }
    token = jwt.encode(payload, JWT_SECRET,algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token:str):
    """
    Decodes the JWT Token
    :param token: JWT Token
    """
    try:
        decode_token = jwt.decode(token,JWT_SECRET,algorithms=JWT_ALGORITHM)
        return decode_token
    except:
        return{}
    
def get_user_id(token:str):
    """
    Gets the username from the JWT Token
    :param token: JWT Token
    """
    # token = request.headers['X-API-KEY']
    # decoded_token = decodeJWT(token)
    # user_id = decoded_token['user_id']
    user = decodeJWT(token)
    return user['user_id']

# def get_user(token:str):
#     """
#     Gets the username from the JWT Token
#     :param token: JWT Token
#     """
#     user = decodeJWT(token)
#     return user['id']
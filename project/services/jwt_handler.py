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

def signJWT(username:str,password:str):
    """
    Generates the JWT Token
    :param username: username
    :param password: password
    """
    payload = {
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
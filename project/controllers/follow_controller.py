from flask import request
from models.follow_model import follow_user, unfollow_user, check_follow, check_follwed_exist
from config import db_config
from services.jwt_handler import get_user_id


def add_follow():
    """
    Follow a user
    """
    followed_id = request.json.get('followed_id')
    
    token = request.headers['X-API-KEY']
    follower_id = get_user_id(token)

    if not check_follwed_exist(db_config, followed_id):
        return {"error": "User does not exist"}, 400

    if follower_id == followed_id:
        return {"error": "Cannot follow yourself"}, 400

    if not all([follower_id, followed_id]):
        return {"error": "Missing data"}, 400

    if check_follow(db_config, follower_id, followed_id):
        return {"error": "Already following the user"}, 400
    
    follow_user(db_config, follower_id, followed_id)
    return {"message": "Successfully followed the user"}, 201

def remove_follow():
    """
    Unfollow a user
    """

    followed_id = request.json.get('followed_id')
    
    token = request.headers['X-API-KEY']
    follower_id = get_user_id(token)
    
    if not check_follwed_exist(db_config, followed_id):
        return {"error": "User does not exist"}, 400

    if follower_id == followed_id:
        return {"error": "Cannot unfollow yourself"}, 400

    if not all([follower_id, followed_id]):
        return {"error": "Missing data"}, 400
    
    if not check_follow(db_config, follower_id, followed_id):
        return {"error": "Not following the user"}, 400

    unfollow_user(db_config, follower_id, followed_id)
    return {"message": "Successfully unfollowed the user"}, 201

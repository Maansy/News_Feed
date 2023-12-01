from flask import request
from models.post_model import create_post, get_all_posts, get_post_by_id, update_post_by_id,delete_post_by_id
from services.jwt_handler import get_user_id
from config import db_config

def add_post():
    """
    Add a new post
    """
    data = request.get_json()
    
    token = request.headers['X-API-KEY']    
    
    user_id = get_user_id(token)
    
    content = data.get('content')

    if not all([user_id, content]):
        return {"error": "Missing data"}, 400

    create_post(db_config, user_id, content)
    return {"message": "Post created successfully"}, 201

def list_posts():
    """
    List all posts of a user
    """
    token = request.headers['X-API-KEY']    
    
    user_id = get_user_id(token)

    posts = get_all_posts(db_config,user_id)
    
    return posts, 200

def get_post(post_id):
    """
    Get a post by id
    :param post_id: post id
    """
    token = request.headers['X-API-KEY']    
    
    user_id = get_user_id(token)
    
    post = get_post_by_id(db_config, post_id, user_id)
    return post, 200

def update_post(post_id):
    """
    Update a post by id
    :param post_id: post id
    """
    data = request.get_json()
    
    token = request.headers['X-API-KEY']    
    
    user_id = get_user_id(token)
    
    content = data.get('content')

    if not all([user_id, content]):
        return {"error": "Missing data"}, 400

    update_post_by_id(db_config, post_id, user_id, content)
    return {"message": "Post updated successfully"}, 201

def delete_post(post_id):
    """
    Delete a post by id
    :param post_id: post id
    """
    token = request.headers['X-API-KEY']    
    
    user_id = get_user_id(token)
    
    delete_post_by_id(db_config, post_id, user_id)
    return {"message": "Post deleted successfully"}, 200
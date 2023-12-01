from flask import request
from models.comment_model import create_comment, edit_comment, delete_comment, check_comment
from models.post_model import check_post
from config import db_config
from services.jwt_handler import get_user_id
def add_comment():
    """
    Add a comment
    :param user_id: user id
    :param post_id: post id
    """
    token = request.headers['X-API-KEY']
    user_id = get_user_id(token)
    data = request.get_json()
    post_id = data.get('post_id')
    content = data.get('content')
    
    if not all([user_id, post_id, content]):
        return {"error": "Missing data"}, 400
    
    if check_post(db_config, post_id):
        create_comment(db_config, user_id, post_id, content)
        return {"message": "Comment created successfully"}, 201
    else:
        return {"error": "Post not found"}, 404
    
def update_comment(comment_id):
    """
    Update a comment
    :param comment_id: comment id
    """
    token = request.headers['X-API-KEY']
    user_id = get_user_id(token)
    data = request.get_json()
    content = data.get('content')

    if not all([user_id, content]):
        return {"error": "Missing data"}, 400
    
    if check_comment(db_config, comment_id, user_id):
        edit_comment(db_config, comment_id, content)
        return {"message": "Comment updated successfully"}, 200
    else:
        return {"error": "Comment not found"}, 404
    
def delete_comment_by_id(comment_id):
    """
    Delete a comment
    :param comment_id: comment id
    """
    token = request.headers['X-API-KEY']
    user_id = get_user_id(token)
    
    if check_comment(db_config, comment_id, user_id):
        delete_comment(db_config,comment_id)
        return {"message": "Comment deleted successfully"}, 200
    else:
        return {"error": "Comment not found"}, 404


from flask_restx import Namespace, Resource, fields
from config import db_config
from controllers.comment_controller import add_comment, update_comment, delete_comment_by_id
from services.token_request import token_required

comment_ns = Namespace('Comment', description='Comment operations')

comment_model = comment_ns.model('Comment', {
    'post_id': fields.Integer(required=True, description='Post id'),
    'content': fields.String(required=True, description='Comment content')
})

comment_update_model = comment_ns.model('CommentUpdate', {
    'content': fields.String(required=True, description='Comment content')
})

comment_delete_model = comment_ns.model('CommentDelete', {
    'comment_id': fields.Integer(required=True, description='Comment id')
})

@comment_ns.route('/')
class Comment(Resource):
   
    @comment_ns.doc(security='News Feed')
    @comment_ns.expect(comment_model, validate=True)
    @token_required
    def post(self):
        """
        Add a new comment
        """
        return add_comment()
    

@comment_ns.route('/<int:comment_id>')
class Comment(Resource):
    
    @comment_ns.doc(security='News Feed')
    @comment_ns.expect(comment_update_model, validate=True)
    @token_required
    def put(self, comment_id):
        """
        Update a comment
        :param comment_id: comment id
        """
        return update_comment(comment_id)
    
    @comment_ns.doc(security='News Feed')
    @token_required
    def delete(self, comment_id):
        """
        Delete a comment
        :param comment_id: comment id
        """
        return delete_comment_by_id(comment_id)

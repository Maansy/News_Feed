from flask_restx import Namespace, Resource
from controllers.post_controller import add_post, list_posts, get_post, update_post, delete_post
from services.token_request import token_required
from flask_restx import fields


post_ns = Namespace('Post', description='Post operations')

get_posts_model = post_ns.model('Post', {
    'post_id': fields.Integer(description='The post unique identifier'),
    'content': fields.String(description='The post content')
})

post_model = post_ns.model('Post', {
    'content': fields.String(description='The post content')
})

post_update_model = post_ns.model('PostUpdate', {
    'content': fields.String(required=True, description='The updated content of the post'),
})

@post_ns.route('/')
class PostList(Resource):
    
    @post_ns.doc(security='News Feed')
    @token_required
    @post_ns.marshal_list_with(get_posts_model)
    def get(self):
        """
        List all posts of a user
        """
        posts, status_code = list_posts()
        return posts, status_code    

    @post_ns.doc(security='News Feed')
    @token_required
    @post_ns.expect(post_model, validate=True)
    def post(self):
        """
        Add a new post
        """
        return add_post()
    
@post_ns.route('/<int:post_id>')
class Post(Resource):
    
    @post_ns.doc(security='News Feed')
    @token_required
    @post_ns.marshal_with(get_posts_model)
    def get(self, post_id):
        """
        Get a post by id
        :param post_id: post id
        """
        post, status_code = get_post(post_id)
        return post, status_code
    
    @post_ns.doc(security='News Feed')
    @token_required
    @post_ns.expect(post_update_model, validate=True)
    def put(self, post_id):
        """
        Update a post by id
        :param post_id: post id
        """

        return update_post(post_id)
    
    @post_ns.doc(security='News Feed')
    @token_required
    def delete(self, post_id):
        """
        Delete a post by id
        :param post_id: post id
        """
        return delete_post(post_id)

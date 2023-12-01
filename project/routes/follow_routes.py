from flask_restx import Namespace, Resource
from controllers.follow_controller import add_follow, remove_follow
from services.token_request import token_required
from flask_restx import fields

follow_ns = Namespace('Follow', description='User follow operations')

follow_model = follow_ns.model('Follow', {
    'followed_id': fields.Integer(description='The followed id')
})

@follow_ns.route('/')
class Follow(Resource):
    
    @follow_ns.doc(security='News Feed')
    @token_required
    @follow_ns.expect(follow_model, validate=True)
    def post(self):
        """
        Follow a user
        """
        return add_follow()
    
    @follow_ns.doc(security='News Feed')
    @token_required
    @follow_ns.expect(follow_model, validate=True)
    def delete(self):
        """
        Unfollow a user
        """
        return remove_follow()
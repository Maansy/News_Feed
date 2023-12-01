
from controllers.auth_controller import register, login
from flask_restx import Namespace, Resource, fields
from services.token_request import token_required
from flask import session
auth_ns = Namespace('User', description='User Authentication')

user_model = auth_ns.model('User', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The user password'),
    'email': fields.String(required=True, description='The user email')
})

user_login_model = auth_ns.model('User Login', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The user password')
})

@auth_ns.route('/register')
class Register(Resource):
    @auth_ns.expect(user_model, validate=True)
    def post(self):
        """
        Register user endpoint
        """
        response, status_code = register()
        return response, status_code


@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(user_login_model, validate=True)
    def post(self):
        """
        Login user endpoint
        """
        response, status_code = login()
        return response, status_code


# @auth_ns.route('/logout')
# class Logout(Resource):
#     @auth_ns.doc(security='News Feed')
#     @token_required
#     def post(self):
#         """
#         Logout user endpoint
#         """
#         return {"message": "User logged out successfully"}, 200
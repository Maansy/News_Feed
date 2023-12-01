from flask import Flask, request, jsonify
import pymysql
import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restx import Api
from config import db_config
from flask_restx import Resource
from routes.auth_routes import auth_ns

# Create Flask app
app = Flask(__name__)

authorizations = {
    'News Feed' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'X-API-KEY'
    }
}

api = Api(app, version='1.0', title='My API',
          description='A simple API', doc='/docs/', authorizations=authorizations,)

# add route
api.add_namespace(auth_ns)

# checking the connection to the database
def check_db_connection():
    try:
        conn = pymysql.connect(**db_config)
        return True
    except Exception as e:
        print(e)
        return False

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        '''Get a greeting'''
        return {'hello': 'world'}
    
if __name__ == '__main__':
    app.run(debug=True)
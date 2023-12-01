# News_Feed

## Description
This is a news feed application that allows users to add posts, comments and follow each other.

after running the app, you can find all the endpoints [here](http://127.0.0.1:5000/docs/)

## Installation
1. Clone the repository using `git clone https://github.com/Maansy/News_Feed`
2. Create a virtual environment using `python3 -m venv env`
3. Create .env file and add the following variables:
    - DB_HOST
    - DB_USER
    - DB_PASSWORD
    - DB_NAME
    - JWT_SECRET_KEY
    - JWT_ALGORITHM
4. Activate the virtual environment using `source env/bin/activate`
5. go to the project directory using `cd project`
6. Install the requirements using `pip install -r requirements.txt`
7. Create the database by running create_newsfeed_tables.sql
8. Run the app using `python3 main.py`

## Endpoints
- `/auth/login` - POST
- `/auth/register` - POST
- `/post/` - GET, POST
- `/post/<int:post_id>` - GET, PUT, DELETE
- `/follow/` - POST, DELETE
- `/comment/` - POST
- `/comment/<int:comment_id>` - PUT, DELETE

## Authentication
- JWT

## Database
- MySQL
- MySQL Workbench

## Technologies Used
- Python
- Flask
- Flask-RESTful
- Flask-JWT-Extended
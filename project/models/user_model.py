import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

def check_user_exists(db_config, username):
    """
    Check if user exists
    :param db_config: database configuration
    :param username: username
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM User WHERE username = %s"
            cursor.execute(sql, (username,))
            user = cursor.fetchone()
            if user:
                return True
    except pymysql.MySQLError as e:
        print(f"Error checking user: {e}")
    finally:
        connection.close()
    return False

def register_user(db_config, username, email, password):
    """
    Register user
    :param db_config: database configuration
    :param username: username
    :param email: email
    :param password: password
    """
    password_hash = generate_password_hash(password)
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "INSERT INTO User (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, email, password_hash))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error saving user: {e}")
    finally:
        connection.close()

def login_user(db_config, username, password):
    """
    Login user
    :param db_config: database configuration
    :param username: username
    :param password: password
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM User WHERE username = %s"
            cursor.execute(sql, (username,))
            user = cursor.fetchone()
            if user:
                # Map column names to values
                columns = [col[0] for col in cursor.description]
                user_dict = dict(zip(columns, user))

                if check_password_hash(user_dict['password'], password):
                    return user_dict
    except pymysql.MySQLError as e:
        print(f"Error logging in: {e}")
    finally:
        connection.close()
    return None

def get_all_users(db_config):
    """
    Get all users
    :param db_config: database configuration
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM User"
            cursor.execute(sql)
            users = cursor.fetchall()
            if users:
                # Map column names to values
                columns = [col[0] for col in cursor.description]
                users_list = []
                for user in users:
                    user_dict = dict(zip(columns, user))
                    users_list.append(user_dict)
                return users_list
    except pymysql.MySQLError as e:
        print(f"Error getting users: {e}")
    finally:
        connection.close()
    return None
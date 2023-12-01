import pymysql


def check_follwed_exist(db_config, followed_id):
    """
    Check if a user exists
    :param followed_id: followed id
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM User WHERE user_id = %s"
            cursor.execute(sql, (followed_id,))
            user = cursor.fetchone()
            if user:
                return True
            else:
                return False
    except pymysql.MySQLError as e:
        print(f"Error checking user: {e}")
    finally:
        connection.close()

def check_follow(db_config, follower_id, followed_id):
    """
    Check if a user is following another user
    :param follower_id: follower id
    :param followed_id: followed id
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Follow WHERE follower_id = %s AND followed_id = %s"
            cursor.execute(sql, (follower_id, followed_id))
            follow = cursor.fetchone()
            if follow:
                return True
            else:
                return False
    except pymysql.MySQLError as e:
        print(f"Error checking follow: {e}")
    finally:
        connection.close()

def follow_user(db_config, follower_id, followed_id):
    """
    Follow a user
    :param follower_id: follower id
    :param followed_id: followed id
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "INSERT INTO Follow (follower_id, followed_id) VALUES (%s, %s)"
            cursor.execute(sql, (follower_id, followed_id))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error following user: {e}")
    finally:
        connection.close()

def unfollow_user(db_config, follower_id, followed_id):
    """
    Unfollow a user
    :param follower_id: follower id
    :param followed_id: followed id
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "DELETE FROM Follow WHERE follower_id = %s AND followed_id = %s"
            cursor.execute(sql, (follower_id, followed_id))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error unfollowing user: {e}")
    finally:
        connection.close()
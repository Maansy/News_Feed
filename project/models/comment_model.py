import pymysql


def check_comment(db_config, comment_id, user_id):
    """
    Check if a comment exists
    :param comment_id: comment id
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Comment WHERE comment_id = %s AND user_id = %s"
            cursor.execute(sql, (comment_id, user_id ))
            comment = cursor.fetchone()
            if comment:
                return True
            else:
                return False
    except pymysql.MySQLError as e:
        print(f"Error checking comment: {e}")
    finally:
        connection.close()

def check_post_owner(db_config, post_id, user_id):
    """
    Check if a post belongs to a user
    :param post_id: post id
    :param user_id: user id
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Post WHERE post_id = %s AND user_id = %s"
            cursor.execute(sql, (post_id, user_id))
            post = cursor.fetchone()
            if post:
                return True
            else:
                return False
    except pymysql.MySQLError as e:
        print(f"Error checking post owner: {e}")
    finally:
        connection.close()

def create_comment(db_config, user_id, post_id, content):
    """
    Create a comment
    :param user_id: user id
    :param post_id: post id
    :param content: comment content
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "INSERT INTO Comment (user_id, post_id, content, timestamp) VALUES (%s, %s, %s, NOW())"
            cursor.execute(sql, (user_id, post_id, content))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error creating comment: {e}")
    finally:
        connection.close()

def delete_comment(db_config, comment_id):
    """
    Delete a comment
    :param comment_id: comment id
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "DELETE FROM Comment WHERE comment_id = %s"
            cursor.execute(sql, (comment_id,))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error deleting comment: {e}")
    finally:
        connection.close()

def edit_comment(db_config, comment_id, content):
    """
    Edit a comment
    :param comment_id: comment id
    :param content: comment content
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "UPDATE Comment SET content = %s WHERE comment_id = %s"
            cursor.execute(sql, (content, comment_id))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error editing comment: {e}")
    finally:
        connection.close()
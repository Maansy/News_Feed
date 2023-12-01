import pymysql

def check_post(db_config, post_id):
    """
    Check if a post exists
    :param post_id: post id
    :param user_id: user id
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Post WHERE post_id = %s"
            cursor.execute(sql, (post_id, ))
            post = cursor.fetchone()
            if post:
                return True
            else:
                return False
    except pymysql.MySQLError as e:
        print(f"Error checking post: {e}")
    finally:
        connection.close()


def create_post(db_config, user_id, content):
    """
    Add a new post
    :param user_id: user id
    :param content: post content
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "INSERT INTO Post (user_id, content) VALUES (%s, %s)"
            cursor.execute(sql, (user_id, content))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error creating post: {e}")
    finally:
        connection.close()

def get_all_posts(db_config, user_id):
    """
    List all posts of a user
    :param user_id: user id
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Post WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            posts = cursor.fetchall()
            posts_list = []
            if posts:
                columns = [col[0] for col in cursor.description]
                posts = [dict(zip(columns, post)) for post in posts]
                for post in posts:
                    posts_list.append(post)
            else:
                posts_list = []
            return posts_list
            
    except pymysql.MySQLError as e:
        print(f"Error fetching posts: {e}")
    finally:
        connection.close()

def get_post_by_id(db_config, post_id, user_id):
    """
    Get a post by id
    :param post_id: post id
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Post WHERE post_id = %s AND user_id = %s"
            cursor.execute(sql, (post_id, user_id))
            post = cursor.fetchone()
            if post:
                columns = [col[0] for col in cursor.description]
                post = dict(zip(columns, post))
                return post
            else:
                return None
    except pymysql.MySQLError as e:
        print(f"Error fetching post: {e}")
    finally:
        connection.close()


def update_post_by_id(db_config, post_id, user_id, content):
    """
    Update a post by id
    :param post_id: post id
    :param user_id: user id
    :param content: post content
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "UPDATE Post SET content = %s WHERE post_id = %s AND user_id = %s"
            cursor.execute(sql, (content, post_id, user_id))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error updating post: {e}")
    finally:
        connection.close()

def delete_post_by_id(db_config, post_id, user_id):
    """
    Delete a post by id
    :param post_id: post id
    :param user_id: user id
    """
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            sql = "DELETE FROM Post WHERE post_id = %s AND user_id = %s"
            cursor.execute(sql, (post_id, user_id))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error deleting post: {e}")
    finally:
        connection.close()
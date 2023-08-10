from lib.post import Post
from lib.tag import Tag

class PostRepo:
    def __init__(self, connection):
        self._connection = connection

    def find_by_tags(self, tag):
        rows = self._connection.execute("SELECT posts.id AS post_id, posts.title, tags.id AS tag_id, tags.name  FROM posts " \
                                        "JOIN posts_tags ON posts_tags.post_id = posts.id " \
                                        "JOIN tags ON posts_tags.tag_id = tags.id " \
                                        "WHERE tags.name = %s" , [tag])
        posts = []
        for row in rows:
            post = Post(row["post_id"], row["title"])
            posts.append(post)
        
        return Tag(rows[0]["tag_id"], rows[0]["name"], posts)
    


    def find_by_posts(self, post):
        rows = self._connection.execute("SELECT tags.id AS tag_id, tags.name, posts.id AS post_id, posts.title " \
                                        "FROM tags " \
                                        "JOIN posts_tags ON posts_tags.tag_id = tags.id " \
                                        "JOIN posts ON posts_tags.post_id = posts.id " \
                                        "WHERE posts.title = %s", [post])
        tags = []
        for row in rows:
            tag = Tag(row["tag_id"], row["name"])
            tags.append(tag)

        return Post(rows[0]['post_id'], rows[0]['title'], tags)
        


    
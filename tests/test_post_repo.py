from lib.post_repo import PostRepo
from lib.post import Post
from lib.tag import Tag

def test_find_by_tags(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repo = PostRepo(db_connection)

    tag = repo.find_by_tags('coding')

    assert tag == Tag(1, 'coding' ,[
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(7, 'SQL basics'),
    ])


def test_find_by_posts(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repo = PostRepo(db_connection)

    post = repo.find_by_posts('A foodie week in Spain')

    assert post == Post(6, 'A foodie week in Spain' ,[
        Tag(2, 'travel'),
        Tag(3, 'cooking')
    ])
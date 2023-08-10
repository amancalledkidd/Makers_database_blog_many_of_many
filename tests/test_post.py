from lib.post import Post 

def test_for_intialise(): 
    post = Post(1, "Hi")
    assert post.id == 1
    assert post.title == "Hi"
    
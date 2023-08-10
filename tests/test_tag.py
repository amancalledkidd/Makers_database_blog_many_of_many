from lib.tag import Tag

def test_for_intialise(): 
    tag = Tag(1, "Hi")
    assert tag.id == 1
    assert tag.name == "Hi"

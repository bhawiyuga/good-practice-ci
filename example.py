def add(a,b):
    return a+b

def subsctract(a,b):
    return a-b

def test_add():
    assert add(2,3) == 5
    assert add(0,0) == 0
    assert add(6,5) == 11

def test_subsctract():
    assert subsctract(2,3) == -1
    assert subsctract(0,0) == 0
    assert subsctract(6,5) == 1
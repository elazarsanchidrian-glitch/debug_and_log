from calculator import add

def test_add():
    assert add(2,3) == 5

def test_add_fail():
    assert add(2,3) == 6

def test_add_none():
    assert add(1,None) is None

def test_add_str():
    assert add(2,"one") == 3


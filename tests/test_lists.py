from listtypes import StringList, TypeList

def test_string_list():
    try:
        StringList(["Hello", "World"])
        assert True
    except:
        assert False

    try:
        StringList(["Hello", 0])
        assert False
    except:
        assert True

class Custom():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class CustomList(TypeList):
    def __init__(self, arr: list = []):
        super().__init__(Custom, arr)

def test_custom_list():
    try:
        CustomList([Custom(1, 2), Custom(4, 6)])
        assert True
    except:
        assert False

    try:
        CustomList([Custom(21, 41), 0])
        assert False
    except:
        assert True
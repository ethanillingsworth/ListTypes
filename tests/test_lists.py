from listtypes import StringList

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
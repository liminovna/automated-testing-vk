import pytest


class TestTuple:

    def test_tuple_len(self):
        assert len(("apple", "banana", "cherry")) == 3

    def test_first_item(self):
        assert ("apple", "banana", "cherry")[0]=="apple"

    def test_one_item_tuple(self):
        assert isinstance(('apple',), tuple)
            

class TestInt:

    # parametrized test
    @pytest.mark.parametrize("num,bool", [
        (-1, True),
        (0, True),
        (2.4, False),
        (-2.4, False),

    ])
    def test_is_int(self, num, bool):
        assert isinstance(num, int) is bool

    def test_float_to_int(self):
        assert int(5.8)==5

    def test_str_to_int(self):
        assert int('2')==2        
        # valid test which throws an error
        try:
            assert int('apple')
        except ValueError:
            pass
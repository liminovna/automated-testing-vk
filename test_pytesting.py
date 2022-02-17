import pytest


class TestTuple:

    def test_tuple_len(self):
        assert len(("apple", "banana", "cherry")) == 3

    # parametrized test
    @pytest.mark.parametrize("tuple,first_item", [
        (("apple", "banana", "cherry"), "apple"),
        ((0, 1, 2, 3, 4, 5), 0),
        ((str, float), str)

    ])
    def test_first_item(self, tuple, first_item):
        assert tuple[0]==first_item

    def test_one_item_tuple(self):
        assert isinstance(('apple',), tuple)
            

class TestInt:

    def test_abs_value(self):
        assert abs(-1) == 1

    def test_float_to_int(self):
        assert int(5.8)==5

    def test_str_to_int(self):
        assert int('2')==2        
        # valid test which throws an error
        try:
            assert int('apple')
        except ValueError:
            pass
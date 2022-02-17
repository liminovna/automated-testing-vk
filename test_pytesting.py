import pytest


class TestTuple:

    def test_tuple_len(self):
        assert len(("apple", "banana", "cherry")) == 3
        assert len((1, 2, 3, 4, 5)) == 5

    # parametrized test
    @pytest.mark.parametrize("tuple,first_item", [
        (("apple", "banana", "cherry"), "apple"),
        ((1, 2, 3, 4, 5), 1),

    ])
    def test_first_item(self, tuple, first_item):
        assert tuple[0]==first_item

    def test_one_item_tuple(self):
        assert isinstance(('apple',), tuple)
            

class TestInt:

    def test_to_string(self):
        assert str(2) == '2'

    def test_addition(self):
        assert 5+10==15

    def test_float_to_int(self):
        assert int(4.8)==4
        assert int(-1)==-1
        assert int('2')==2
        
        # valid test which throws an error
        try:
            assert int('apple')
        except ValueError:
            pass
import pytest

from collection.bag import Bag


def test_bag_add():
    b = Bag()
    assert b.size == 0

    test_datas = [1, 'a', 0x123, None]

    for index, item in enumerate(test_datas):
        b.add(item)
        assert b.size == index + 1


def test_bag_remove():
    b = Bag()
    test_datas = [1, 'a', 0x123, None]
    with pytest.raises(ValueError):
        while True:
            assert b.remove() in test_datas

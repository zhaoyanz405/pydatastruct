from collection.stack import Stack


def test_stack_push():
    s = Stack()
    assert s.size == 0

    s.push(1)
    assert s.size == 1

    v = s.pop()
    assert v == 1
    assert s.size == 0

    s.push('test')
    s.push(None)

    assert s.size == 2

    assert s.pop() is None
    assert s.pop() == 'test'


def test_iter_stack():
    s = Stack()
    test_datas = [1, 2, 3, 4, 5]
    for x in test_datas:
        s.push(x)

    for item in s:
        assert item == test_datas.pop()

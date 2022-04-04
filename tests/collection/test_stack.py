import pytest

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


def test_stack_iteration():
    s = Stack()
    test_datas = [1, 2, 3, 4, 5]
    reverse_td = [5, 4, 3, 2, 1]
    for x in test_datas:
        s.push(x)

    for idx, item in enumerate(s):
        assert item == reverse_td[idx]

    iter(s)
    assert s._cur_node is None

    for idx, item in enumerate(s):
        assert item == reverse_td[idx]


def test_stack_iter_exception():
    s = Stack()
    with pytest.raises(StopIteration):
        next(s)


def test_stack_parentheses_correct():
    match_map = {
        '[': ']',
        '{': '}',
        '(': ')',
    }
    inputs = "[()]{}{[()()]()}"
    s = Stack()
    for i in inputs:
        if s.is_empty():
            s.push(i)
        else:
            if match_map[s.first.item] == i:
                s.pop()
            else:
                s.push(i)
        try:
            print(list(s))
        except AttributeError:
            print("empty stack")

    assert s.size == 0


def test_stack_parentheses_wrong():
    match_map = {
        '[': ']',
        '{': '}',
        '(': ')',
    }
    inputs = "[{})"

    s = Stack()
    for i in inputs:
        if s.is_empty():
            s.push(i)
        else:
            if match_map[s.first.item] == i:
                s.pop()
            else:
                s.push(i)

    assert s.size != 0

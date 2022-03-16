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

    assert s.pop() == None
    assert s.pop() == 'test'

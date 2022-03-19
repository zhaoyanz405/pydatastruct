import pytest

from collection.queue import Queue, EmptyQueueError


def test_queue():
    q = Queue()

    test_value = 'test'
    q.enqueue(test_value)
    actual_value = q.dequeue()
    assert test_value == actual_value


def test_queue_is_empty():
    q = Queue()
    assert q.is_empty()

    q.enqueue(None)
    assert not q.is_empty()


def test_queue_enqueue_from_empty():
    q = Queue()

    with pytest.raises(EmptyQueueError):
        q.dequeue()


def test_iter_queue():
    q = Queue()

    test_datas = [1, 2, 3, 4, 5]
    for x in test_datas:
        q.enqueue(x)

    for index, item in enumerate(q):
        assert item == test_datas[index]

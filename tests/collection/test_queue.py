import pytest

from collection.queue import Queue, EmptyQueueError


def test_queue_put_and_get():
    q = Queue()

    test_value = 'test'
    q.put(test_value)
    actual_value = q.get()
    assert test_value == actual_value


def test_queue_is_empty():
    q = Queue()
    assert q.is_empty()

    q.put(None)
    assert not q.is_empty()


def test_queue_get_from_empty():
    q = Queue()

    with pytest.raises(EmptyQueueError):
        q.get()

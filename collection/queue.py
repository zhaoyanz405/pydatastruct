"""
FIFO
"""
from collection.node import Node


class EmptyQueueError(Exception):
    pass


class ListQueue:

    def __init__(self):
        self.data = []
        self._idx = 0

    @property
    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError

        v = self.data[0]
        del self.data[0]
        return v

    def __next__(self):
        try:
            value = self.data[self._idx]
        except IndexError:
            raise StopIteration

        self._idx += 1

        return value

    def __iter__(self):
        self._idx = 0
        return self


class NodeQueue:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        self._cur_node = None

    def is_empty(self):
        return self.first is None

    def enqueue(self, item):
        node = Node()
        node.item = item

        if self.is_empty():
            self.first = node
            self.last = self.first
        else:
            self.last.next = node
            self.last = self.last.next

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            self.last = None
            raise EmptyQueueError

        item = self.first.item
        self.first = self.first.next

        self.size -= 1
        return item

    def __next__(self):
        if self.is_empty():
            raise StopIteration

        if self._cur_node is None:
            self._cur_node = self.first
        else:
            self._cur_node = next(self._cur_node)

        return self._cur_node.item

    def __iter__(self):
        self._cur_node = None
        return self


Queue = ListQueue

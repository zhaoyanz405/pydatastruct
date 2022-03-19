"""
FIFO
"""
from collection.node import Node, iter_nodes


class EmptyQueueError(Exception):
    pass


class Queue:

    def __init__(self):
        self.data = []

    @property
    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size == 0

    def put(self, item):
        self.data.append(item)

    def get(self):
        if self.is_empty():
            raise EmptyQueueError

        v = self.data[0]
        del self.data[0]
        return v


class NodeQueue:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

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

    def __iter__(self):
        return iter_nodes(self.first)


Queue = NodeQueue

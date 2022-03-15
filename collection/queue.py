"""
FIFO
"""


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

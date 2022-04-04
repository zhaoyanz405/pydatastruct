from collection.node import Node


class Stack:
    def __init__(self):
        self.first = None
        self.size = 0
        self._cur_node = None

    def is_empty(self):
        return self.first is None

    def push(self, item):
        new_node = Node()
        new_node.item = item

        new_node.next = self.first
        self.first = new_node

        self.size += 1

    def pop(self):
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
